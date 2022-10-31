# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from contextlib import contextmanager
from typing import Dict, List, Optional
from requests import Session
from requests.utils import add_dict_to_cookiejar
from requests.cookies import RequestsCookieJar
from uuid import uuid4
from jwt import encode as jwtEncode

from pjsekai.models.systemInfo import SystemInfo
from pjsekai.assetBundle import AssetBundle
from pjsekai.exceptions import *
from pjsekai.enums.tutorialStatus import TutorialStatus
from pjsekai.enums.platform import Platform
from pjsekai.utilities import encrypt, decrypt, msgpack, unmsgpack

class API:

    _platform: Platform
    _session: Session
    domains: Dict[str, str]
    _key: bytes
    _iv : bytes
    _jwtSecret: str
    systemInfo: SystemInfo
    _sessionToken: Optional[str]
    _userId: Optional[str]
    enableEncryption: Dict[str,bool]

    @property
    def platform(self) -> Platform:
        return self._platform
    @property
    def session(self) -> Session:
        return self._session

    DEFAULT_DOMAINS: Dict[str, str] = {
        "api": "production-game-api.sekai.colorfulpalette.org",
        "asset": "assetbundle.sekai.colorfulpalette.org",
        "assetBundleInfo": "assetbundle-info.sekai.colorfulpalette.org",
        "gameVersion": "game-version.sekai.colorfulpalette.org",
        "signature": "issue.sekai.colorfulpalette.org",
    }

    DEFAULT_ENCRYPTION: Dict[str, bool] = {
        "api": True,
        "asset": False,
        "assetBundleInfo": True,
        "gameVersion": True,
        "signature": True,
    }

    DEFAULT_CHUNK_SIZE: int = 1024 * 1024

    def __init__(
        self, 
        platform: Platform, 
        key: bytes, 
        iv: bytes, 
        jwtSecret: str, 
        systemInfo: Optional[SystemInfo],
        domains: Optional[Dict[str, str]] = None, 
        enableEncryption: Optional[Dict[str,bool]] = None,
    ) -> None:
        self._platform = platform
        self._session = Session()
        self.domains = self.DEFAULT_DOMAINS.copy()
        if domains is not None:
            self.domains.update(domains)
        self._key = key
        self._iv = iv
        self._jwtSecret = jwtSecret
        self._systemInfo = SystemInfo()
        if systemInfo is not None:
            self.systemInfo = systemInfo
        self._sessionToken = None
        self._userId = None
        self.enableEncryption = self.DEFAULT_ENCRYPTION.copy()
        if enableEncryption is not None:
            self.enableEncryption.update(enableEncryption)

    def _pack(self, plaintextDict: Optional[dict], enableEncryption: bool = True) -> bytes:
        plaintext: bytes = msgpack(plaintextDict)
        return encrypt(plaintext, self._key, self._iv) if enableEncryption else plaintext

    def _unpack(self, ciphertext: bytes, enableDecryption: bool = True) -> dict:
        plaintext: bytes = decrypt(ciphertext, self._key, self._iv) if enableDecryption else ciphertext
        return unmsgpack(plaintext)

    def _generateHeaders(self, systemInfo: Optional[SystemInfo] = None) -> dict:
        appVersion: Optional[str]
        dataVersion: Optional[str]
        assetVersion: Optional[str]
        if systemInfo is None:
            appVersion = self.systemInfo.appVersion
            dataVersion = self.systemInfo.dataVersion
            assetVersion = self.systemInfo.assetVersion
        else:
            appVersion = systemInfo.appVersion
            dataVersion = systemInfo.dataVersion
            assetVersion = systemInfo.assetVersion
        return {
            "Content-Type": "application/octet-stream",
            "Accept": "application/octet-stream",
            "X-App-Version": appVersion,
            "X-Data-Version": dataVersion,
            "X-Asset-Version": assetVersion,
            "X-Request-Id": str(uuid4()),
            "X-Unity-Version": self.platform.unityVersion,
            
            **({} if self._sessionToken is None else {
                "X-Session-Token": self._sessionToken,
            }),
            **self.platform.headers,
        }

    def getSignedCookie(self, systemInfo: Optional[SystemInfo] = None) -> RequestsCookieJar:
        url: str = f"https://{self.domains['signature']}/api/signature"
        encrypt: bool = self.enableEncryption.get("signature",True)
        with self.session.post(
            url,
            headers=self._generateHeaders(systemInfo),
            data=self._pack(None,encrypt)
        ) as response:
            cookies = {k:v for k,v in (cookie.split("=") for cookie in (c.strip() for c in response.headers["Set-Cookie"].split(";")) if cookie!="")}
            response.raise_for_status()
            self.session.cookies
            return add_dict_to_cookiejar(self.session.cookies, cookies)

    def getAssetBundleInfo(self, assetVersion: Optional[str] = None, systemInfo: Optional[SystemInfo] = None) -> dict:
        if assetVersion is None:
            if systemInfo is None:
                assetVersion = self.systemInfo.assetVersion
            else:
                assetVersion = systemInfo.assetVersion
        url: str = f"https://{self.domains['assetBundleInfo']}/api/version/{assetVersion}/os/{self.platform.assetOS.value}"
        encrypt: bool = self.enableEncryption.get("assetBundleInfo",False)
        with self.session.get(url,headers=self._generateHeaders(systemInfo)) as response:
            if response.status_code == 426:
                raise UpdateRequired
            elif response.status_code == 403:
                raise SessionExpired
            response.raise_for_status()
            return self._unpack(response.content, encrypt)

    @contextmanager
    def downloadAssetBundle(self, assetBundleName: str, chunkSize: Optional[int] = None, systemInfo: Optional[dict] = None):
        if chunkSize is None:
            chunkSize = self.DEFAULT_CHUNK_SIZE
        assetVersion: Optional[str] = self.systemInfo.assetVersion
        assetHash: Optional[str] = self.systemInfo.assetHash
        if systemInfo is not None:
            assetVersion = systemInfo["assetVersion"]
            assetHash = systemInfo["assetHash"]
        if assetVersion is None or assetHash is None:
            raise UpdateRequired
        url: str = f"https://{self.domains['asset']}/{assetVersion}/{assetHash}/android/{assetBundleName}"
        encrypt: bool = self.enableEncryption.get("asset",False)
        if encrypt:
            raise NotImplementedError
        response = self.session.get(url, stream=True)
        try:
            if response.status_code == 426:
                raise UpdateRequired
            elif response.status_code == 403:
                raise SessionExpired
            response.raise_for_status()
            yield AssetBundle(obfuscatedChunks=response.iter_content(chunk_size=chunkSize))
        finally:
            response.close()

    def request(self, method: str, path: str, params: Optional[dict] = None, data: Optional[dict] = None, headers: Optional[dict] = None, isAuthenticationRequired: bool = False, systemInfo: Optional[SystemInfo] = None) -> dict:
        if isAuthenticationRequired and (self._sessionToken == None or self._userId == None):
            raise NotAuthenticatedException(
                "Authentication required")
        url: str = f"https://{self.domains['api']}/api/{path}"
        encrypt: bool = self.enableEncryption.get("api",True)
        with self.session.request(
            method,
            url,
            headers={
                **self._generateHeaders(systemInfo),
                **({} if headers is None else headers),
            },
            params=params,
            data=self._pack(data,encrypt) if data is not None or method.casefold()=="POST".casefold() else None
        ) as response:
            if response.status_code == 426:
                raise UpdateRequired
            elif response.status_code == 403:
                raise SessionExpired
            response.raise_for_status()
            self._sessionToken = response.headers.get("X-Session-Token", self._sessionToken)
            return self._unpack(response.content,encrypt)
    
    def ping(self) -> dict:
        return self.request("GET","")

    def getSystemInfo(self) -> dict:
        return self.request("GET", "system")
    
    def register(self) -> dict:
        return self.request("POST", "user", data = self.platform.info)

    def authenticate(self, userId: str, credential: str) -> dict:
        self._userId = userId
        responseDict: dict = self.request("PUT", f"user/{userId}/auth", data = { "credential": credential })
        self._sessionToken = responseDict["sessionToken"]
        return responseDict

    def getMasterData(self, dataVersion: Optional[str] = None) -> dict:
        if dataVersion is None:
            return self.request("GET", f"suite/master")
        else:
            return self.request("GET", f"suite/master", systemInfo=self.systemInfo.copy(update={"dataVersion":dataVersion}))

    def getNotices(self) -> dict:
        return self.request("GET", f"information")

    def getUserData(self, name: Optional[str] = None) -> dict:
        params = {
            "isForceAllReload": name is None,
            "name": name,
        }
        return self.request("GET", f"suite/user/{self._userId}", params=params, isAuthenticationRequired = True)
    
    def getLoginBonus(self) -> dict:
        return self.request("PUT", f"user/{self._userId}/home/refresh", data = {
            "refreshableTypes":[
                "new_pending_friend_request",
                "login_bonus"
            ]
        }, isAuthenticationRequired=True)

    def getProfile(self, userId: Optional[str] = None) -> dict:
        if userId is None:
            userId = self._userId
        return self.request("GET", f"user/{userId}/profile", isAuthenticationRequired = True)

    def setTutorialStatus(self, tutorialStatus: TutorialStatus) -> dict:
        return self.request("PATCH", f"user/{self._userId}/tutorial", data = { "tutorialStatus": tutorialStatus.value }, isAuthenticationRequired = True)

    def generateTransferCode(self, password: str) -> dict:
        return self.request("PUT", f"user/{self._userId}/inherit", data = { "password": password }, isAuthenticationRequired = True)

    def checkTransferCode(self, transferCode: str, password: str) -> dict:
        tokenPayload = {
            "inheritId": transferCode,
            "password": password
        }
        header = {
            "x-inherit-id-verify-token": jwtEncode(tokenPayload, self._jwtSecret, algorithm="HS256"),
        }
        params = {
            "isExecuteInherit": False,
        }
        return self.request("POST", f"inherit/user/{transferCode}", params=params, headers=header)

    def generateCredential(self, transferCode: str, password: str) -> dict:
        tokenPayload = {
            "inheritId": transferCode,
            "password": password
        }
        header = {
            "x-inherit-id-verify-token": jwtEncode(tokenPayload, self._jwtSecret, algorithm="HS256"),
        }
        params = {
            "isExecuteInherit": True,
        }
        return self.request("POST", f"inherit/user/{transferCode}", params=params, headers=header)

    def gacha(self, gachaId: int, gachaBehaviorId: int) -> dict:
        return self.request("PUT", f"user/{self._userId}/gacha/{gachaId}/gachaBehaviorId/{gachaBehaviorId}", isAuthenticationRequired = True)

    def receivePresents(self, presentIds: List[str]) -> dict:
        return self.request("POST", f"user/{self._userId}/present", data = {
            "presentIds": presentIds
        }, isAuthenticationRequired = True)

    def startSoloLive(self, musicId: int, musicDifficultyId: int, musicVocalId: int, deckId: int, boostCount: int, isAuto: bool) -> dict:
        return self.request("POST", f"user/{self._userId}/live", data = {
            "musicId": musicId,
            "musicDifficultyId": musicDifficultyId,
            "musicVocalId": musicVocalId,
            "deckId": deckId,
            "boostCount": boostCount,
            "isAuto": isAuto
        }, isAuthenticationRequired = True)

    def endSoloLive(self, liveId:str, score: int, perfectCount: int, greatCount: int, goodCount: int, badCount: int, missCount: int, maxCombo: int, life: int, tapCount: int, continueCount: int) -> dict:
        return self.request("PUT", f"user/{self._userId}/live/{liveId}", data = {
            "score": score,
            "perfectCount": perfectCount,
            "greatCount": greatCount,
            "goodCount": goodCount,
            "badCount": badCount,
            "missCount": missCount,
            "maxCombo": maxCombo,
            "life": life,
            "tapCount": tapCount,
            "continueCount": continueCount
        }, isAuthenticationRequired = True)

    def getEventRankings(self, eventId: int, targetUserId: Optional[str] = None, targetRank: Optional[int] = None, higherLimit: Optional[int] = None, lowerLimit: Optional[int] = None) -> dict:
        if targetUserId is None and targetRank is None:
            targetUserId = self._userId
        params = {
            "targetUserId": targetUserId,
            "targetRank": targetRank,
            "higherLimit": higherLimit,
            "lowerLimit": lowerLimit,
        }
        return self.request("GET", f"user/{self._userId}/event/{eventId}/ranking", params=params, isAuthenticationRequired = True)

    def getEventTeamsPlayerCount(self, eventId: int) -> dict:
        return self.request("GET", f"cheerful-carnival-team-count/{eventId}", isAuthenticationRequired=True)

    def getEventTeamsPoint(self, eventId: int) -> dict:
        return self.request("GET", f"cheerful-carnival-team-point/{eventId}", isAuthenticationRequired=True)

    def getRankMatchRankings(self, rankMatchSeasonId: int, targetUserId: Optional[str] = None, targetRank: Optional[int] = None, higherLimit: Optional[int] = None, lowerLimit: Optional[int] = None) -> dict:
        if targetUserId is None and targetRank is None:
            targetUserId = self._userId
        params = {
            "targetUserId": targetUserId,
            "targetRank": targetRank,
            "higherLimit": higherLimit,
            "lowerLimit": lowerLimit,
        }
        return self.request("GET", f"user/{self._userId}/rank-match-season/{rankMatchSeasonId}/ranking", params=params, isAuthenticationRequired = True)

    def getRoomInvitations(self) -> dict:
        return self.request("GET", f"user/{self._userId}/invitation", isAuthenticationRequired=True)
    
    def sendFriendRequest(self, targetUserId: str, message: Optional[str] = None) -> dict:
        return self.request("POST", f"user/{self._userId}/friend/{targetUserId}", data={
            "message": message, 
            "friendRequestSentLocation": "id_search",
        }, isAuthenticationRequired=True)

    def rejectFriendRequest(self, requestUserId: str) -> dict:
        params = {
            "type": "reject_friend_request",
        }
        return self.request("DELETE", f"user/{self._userId}/friend/{requestUserId}", params=params, isAuthenticationRequired=True)

    def acceptFriendRequest(self, requestUserId: str) -> dict:
        return self.request("PUT", f"user/{self._userId}/friend/{requestUserId}", isAuthenticationRequired=True)

    def removeFriend(self, friendUserId: str) -> dict:
        params = {
            "type": "release_friend",
        }
        return self.request("DELETE", f"user/{self._userId}/friend/{friendUserId}", params=params, isAuthenticationRequired=True)
