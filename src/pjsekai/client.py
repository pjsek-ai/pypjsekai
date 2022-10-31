# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional, List
from json import load, dump, JSONDecodeError
from pydantic.json import pydantic_encoder

from pjsekai.models import *
from pjsekai.enums import *
from pjsekai.api import API
from pjsekai.asset import Asset
from pjsekai.exceptions import *
from pjsekai.utilities import *
from pjsekai.live import *


class Client:

    _key: bytes
    _iv: bytes
    _hcaKey: bytes
    _jwtSecret: str
    _platform: Platform
    _systemInfoFilePath: Optional[str]
    _masterDataFilePath: Optional[str]
    _userDataFilePath: Optional[str]
    _assetsPath: Optional[str]
    _asset: Optional[Asset]
    _systemInfo: SystemInfo
    _userId: Optional[str]
    _credential: Optional[str]
    _masterData: MasterData
    _userData: dict

    @property
    def platform(self) -> Platform:
        return self._platform
    @property
    def domains(self) -> Dict[str,str]:
        return self.apiManager.domains
    @property 
    def DEFAULT_DOMAINS(self) -> Dict[str,str]:
        return self.apiManager.DEFAULT_DOMAINS
    @property
    def enableEncryption(self) -> Dict[str,bool]:
        return self.apiManager.enableEncryption
    @property 
    def DEFAULT_ENCRYPTION(self) -> Dict[str,bool]:
        return self.apiManager.DEFAULT_ENCRYPTION
    @property
    def systemInfo(self) -> SystemInfo:
        return self._systemInfo
    @systemInfo.setter
    def systemInfo(self, newValue: SystemInfo) -> None:
        self._systemInfo = newValue
        if self._systemInfoFilePath is not None:
            with open(self._systemInfoFilePath, "w") as f:
                dump(newValue,f,indent=2,ensure_ascii=False,default=pydantic_encoder)
    @property
    def userId(self) -> Optional[str]:
        return self._userId
    @property
    def credential(self) -> Optional[str]:
        return self._credential
    @property
    def isLoggedIn(self) -> bool:
        return self._credential is not None
    @property
    def masterData(self) -> MasterData:
        return self._masterData
    @masterData.setter
    def masterData(self, newValue: MasterData) -> None:
        self._masterData = newValue
        if self._masterDataFilePath is not None:
            with open(self._masterDataFilePath, "w") as f:
                dump(newValue,f,indent=2,ensure_ascii=False,default=pydantic_encoder)
    @property
    def userData(self) -> dict:
        return self._userData 
    def _updateUserResources(self, response) -> dict:
        self._userData = {
            **self._userData,
            **response["updatedResources"],
        }
        if self._userDataFilePath is not None:
            with open(self._userDataFilePath, "w") as f:
                dump(self._userData,f,indent=2,ensure_ascii=False)
        del response["updatedResources"]
        return response
    @property
    def asset(self) -> Optional[Asset]:
        return self._asset

    @property
    def now(self) -> Optional[int]:
        return self._userData["now"]
    @property
    def friends(self) -> Optional[List[dict]]:
        if not self.isLoggedIn:
            raise NotAuthenticatedException()
        if "userFriends" not in self._userData:
            return None
        return [friend for friend in self._userData["userFriends"] if friend["friendStatus"]=="friend"]
    @property
    def receivedFriendRequests(self) -> Optional[List[dict]]:
        if not self.isLoggedIn:
            raise NotAuthenticatedException()
        if "userFriends" not in self._userData:
            return None
        return [friend for friend in self._userData["userFriends"] if friend["friendStatus"]=="pending_request"]
    @property
    def sentFriendRequests(self) -> Optional[List[dict]]:
        if not self.isLoggedIn:
            raise NotAuthenticatedException()
        if "userFriends" not in self._userData:
            return None
        return [friend for friend in self._userData["userFriends"] if friend["friendStatus"]=="sent_request"]

    def __init__(
        self, 
        key: bytes, 
        iv: bytes, 
        hcaKey: bytes = b"", 
        jwtSecret: str = "", 
        platform: Platform = Platform.ANDROID, 
        domains: Optional[Dict[str,str]] = None, 
        systemInfoFilePath: Optional[str] = None, 
        masterDataFilePath: Optional[str] = None, 
        userDataFilePath: Optional[str] = None, 
        assetsPath: Optional[str] = None, 
        ensureLatest: bool = False,
        enableEncryption: Optional[Dict[str,bool]] = None,
    ) -> None:
        self._key = key
        self._iv = iv
        self._hcaKey = hcaKey
        self._jwtSecret = jwtSecret
        self._platform = platform
        
        self._systemInfoFilePath = systemInfoFilePath
        self._masterDataFilePath = masterDataFilePath
        self._userDataFilePath = userDataFilePath
        self._assetsPath = assetsPath
        self._asset = None

        if self._systemInfoFilePath is not None:
            try:
                with open(self._systemInfoFilePath, "r") as f:
                    self._systemInfo = SystemInfo(**load(f))
            except (FileNotFoundError, JSONDecodeError):
                self.systemInfo = SystemInfo()
        else:
            self.systemInfo = SystemInfo()

        if self._masterDataFilePath is not None:
            try:
                with open(self._masterDataFilePath, "r") as f:
                    self._masterData = MasterData(**load(f))
            except (FileNotFoundError, JSONDecodeError):
                self.masterData = MasterData()
        else:
            self.masterData = MasterData()

        self._userData = {}
        if self._userDataFilePath is not None:
            try:
                with open(self._userDataFilePath, "r") as f:
                    self._userData = load(f)
            except (FileNotFoundError, JSONDecodeError):
                with open(self._userDataFilePath, "w") as f:
                    dump(self._userData,f,indent=2,ensure_ascii=False)

        self._userId = None
        self._credential = None
        self.apiManager = API(
            platform = platform, 
            domains = domains, 
            key = key, 
            iv = iv, 
            jwtSecret = jwtSecret, 
            systemInfo = self.systemInfo,
            enableEncryption = enableEncryption,
        )
        self.apiManager.getSignedCookie()

        if self.systemInfo.assetVersion is not None and self.systemInfo.assetHash is not None and assetsPath is not None:
            self._asset = Asset(self.systemInfo.assetVersion,self.systemInfo.assetHash,assetsPath)

        if ensureLatest:
            self.ensureLatest()

    def register(self) -> dict:
        response: dict = self.apiManager.register()
        return self._updateUserResources(response)

    def login(self, userId: str, credential: str) -> dict:
        response: dict = self.apiManager.authenticate(userId,credential)
        self._userId = userId
        self._credential = credential
        self.apiManager.getLoginBonus()
        self._userData = self.apiManager.getUserData()
        return self._updateUserResources(response)

    def reloadUserData(self, name: Optional[str] = None) -> dict:
        self._userData = self.apiManager.getUserData(name)
        return self._userData

    def checkVersion(self, bypassAvailability: bool = False) -> SystemInfo:
        response: dict = self.apiManager.getSystemInfo()
        appVersions = [appVersionInfo for appVersionInfo in (SystemInfo(**appVersion) for appVersion in response["appVersions"]) if bypassAvailability or appVersionInfo.appVersionStatus is not AppVersionStatus.NOT_AVAILABLE]
        if len(appVersions) > 0:
            matchingAppVersionInfo = [appVersionInfo for appVersionInfo in appVersions if appVersionInfo.appVersion == self.systemInfo.appVersion]
            if len(matchingAppVersionInfo) > 0:
                info: SystemInfo = matchingAppVersionInfo[-1]
                status: str = "" if info.appVersionStatus is None else info.appVersionStatus.value
                if info.systemProfile != self.systemInfo.systemProfile:
                    self.systemInfo = SystemInfo(
                        systemProfile = info.systemProfile, 
                        appVersion = self.systemInfo.appVersion, 
                        appHash = self.systemInfo.appHash,
                        multiPlayVersion = self.systemInfo.multiPlayVersion,
                        appVersionStatus = status,
                    )
                assetUpdateRequired: bool = info.assetVersion != self.systemInfo.assetVersion or self.asset is None or info.assetVersion != self.asset.version
                if not bypassAvailability and info.appVersionStatus is AppVersionStatus.MAINTENANCE:
                    raise ServerInMaintenance()
                if info.dataVersion is not None and info.assetVersion is not None and info.assetHash is not None and info.dataVersion != self.systemInfo.dataVersion and assetUpdateRequired:
                    raise MultipleUpdatesRequired(info.dataVersion,info.assetVersion,info.assetHash,status)
                elif info.assetVersion is not None and info.assetHash is not None and assetUpdateRequired:
                    raise AssetUpdateRequired(info.assetVersion,info.assetHash)
                elif info.dataVersion is not None and info.dataVersion != self.systemInfo.dataVersion:
                    raise DataUpdateRequired(info.dataVersion,status)
                return info
            elif appVersions[-1].appVersion is not None and appVersions[-1].appHash is not None and appVersions[-1].multiPlayVersion is not None:
                raise AppUpdateRequired(appVersions[-1].appVersion,appVersions[-1].appHash,appVersions[-1].multiPlayVersion)
        raise NoAvailableVersions()
        
    def updateApp(self, appVersion: Optional[str] = None, appHash: Optional[str] = None, multiPlayVersion: Optional[str] = None) -> None:
        if appVersion is None or appHash is None or multiPlayVersion is None:
            try:
                self.checkVersion()
            except AppUpdateRequired as e:
                appVersion = e.appVersion
                appHash = e.appHash
                multiPlayVersion = e.multiPlayVersion
            except (ServerInMaintenance, MultipleUpdatesRequired, AssetUpdateRequired, DataUpdateRequired):
                return
        self.systemInfo = self.systemInfo.copy(update={
            "appVersion": appVersion,
            "appHash": appHash,
            "multiPlayVersion": multiPlayVersion,
        })

    def updateData(self, dataVersion: str, appVersionStatus: str) -> None:
        response: dict = self.apiManager.getMasterData(dataVersion)
        self.masterData = MasterData(**response)
        self.systemInfo = self.systemInfo.copy(update={
            "dataVersion": dataVersion,
            "appVersionStatus": appVersionStatus,
        })

    def updateAsset(self, assetVersion: str, assetHash: str) -> None:
        self._asset = Asset(assetVersion,assetHash,self._assetsPath)
        self._asset.getAssetBundleInfo(self.apiManager)
        self.systemInfo = self.systemInfo.copy(update={
            "assetVersion": assetVersion,
            "assetHash": assetHash,
        })

    def ensureLatest(self) -> bool:
        try:
            self.checkVersion()
        except AppUpdateRequired as e:
            self.updateApp(e.appVersion, e.appHash, e.multiPlayVersion)
            self.apiManager.systemInfo = self.systemInfo
            self.ensureLatest()
            return True
        except MultipleUpdatesRequired as e:
            self.updateAsset(e.assetVersion, e.assetHash)
            self.apiManager.systemInfo = self.systemInfo
            self.updateData(e.dataVersion, e.appVersionStatus)
            self.apiManager.systemInfo = self.systemInfo
            return True
        except AssetUpdateRequired as e:
            self.updateAsset(e.assetVersion, e.assetHash)
            self.apiManager.systemInfo = self.systemInfo
            return True
        except DataUpdateRequired as e:
            self.updateData(e.dataVersion, e.appVersionStatus)
            self.apiManager.systemInfo = self.systemInfo
            return True
        return False


    def refreshSignedCookie(self) -> None:
        self.apiManager.getSignedCookie()

    def ping(self) -> dict:
        return self.apiManager.ping()

    def transferOut(self, password: str) -> dict:
        response: dict = self.apiManager.generateTransferCode(password)
        return self._updateUserResources(response)

    def transferCheck(self, transferCode: str, password: str) -> dict:
        response: dict = self.apiManager.checkTransferCode(transferCode, password)
        return response

    def transferIn(self, transferCode: str, password: str) -> dict:
        response: dict = self.apiManager.generateCredential(transferCode, password)
        userId: str = response["afterUserGamedata"]["userId"]
        credential: str = response["credential"]
        return self.login(userId,credential)

    def advanceTutorial(self, unit: Unit = Unit.LN) -> dict:
        currentTutorialStatus: TutorialStatus = TutorialStatus(self.userData["userTutorial"]["tutorialStatus"])
        response: dict = self.apiManager.setTutorialStatus(currentTutorialStatus.next(unit))
        return self._updateUserResources(response)

    def receivePresent(self, presentId) -> dict:
        response: dict = self.apiManager.receivePresents([presentId])
        return self._updateUserResources(response)

    def receiveAllPresents(self) -> dict:
        response: dict = self.apiManager.receivePresents([present["presentId"] for present in self.userData["userPresents"]])
        return self._updateUserResources(response)

    def gacha(self, gachaId: int, gachaBehaviorId: int) -> dict:
        response: dict = self.apiManager.gacha(gachaId,gachaBehaviorId)
        return self._updateUserResources(response)

    def startSoloLive(self, live: SoloLive):
        response: dict = self.apiManager.startSoloLive(live.musicId, live.musicDifficultyId, live.musicVocalId, live.deckId, live.boostCount, live.isAuto)
        live.start(response["userLiveId"],response["skills"],response["comboCutins"])
        return self._updateUserResources(response)

    def endSoloLive(self, live: SoloLive) -> dict:
        if not live.isActive or live.liveId is None:
            raise LiveNotActive
        if live.life <= 0:
            raise LiveDead
        response: dict = self.apiManager.endSoloLive(live.liveId, live.score, live.perfectCount, live.greatCount, live.goodCount, live.badCount, live.missCount, live.maxCombo, live.life, live.tapCount, live.continueCount)
        live.end()
        return self._updateUserResources(response)

    def getEventRankings(self, eventId: int, targetUserId: Optional[str] = None, targetRank: Optional[int] = None, higherLimit: Optional[int] = None, lowerLimit: Optional[int] = None) -> dict:
        if targetUserId is None and targetRank is None:
            targetUserId = self.userId
        return self.apiManager.getEventRankings(eventId, targetUserId, targetRank, higherLimit, lowerLimit)

    def getEventTeamsPlayerCount(self, eventId: int) -> dict:
        return self.apiManager.getEventTeamsPlayerCount(eventId)

    def getEventTeamsPoint(self, eventId: int) -> dict:
        return self.apiManager.getEventTeamsPoint(eventId)

    def getRankMatchRankings(self, rankMatchSeasonId: int, targetUserId: Optional[str] = None, targetRank: Optional[int] = None, higherLimit: Optional[int] = None, lowerLimit: Optional[int] = None) -> dict:
        if targetUserId is None and targetRank is None:
            targetUserId = self.userId
        return self.apiManager.getRankMatchRankings(rankMatchSeasonId, targetUserId, targetRank, higherLimit, lowerLimit)

    def sendFriendRequest(self, userId: str, message: Optional[str] = None) -> None:
        response: dict = self.apiManager.sendFriendRequest(userId, message)
        self._updateUserResources(response)

    def rejectFriendRequest(self, requestUserId: str) -> None:
        response: dict = self.apiManager.rejectFriendRequest(requestUserId)
        self._updateUserResources(response)

    def acceptFriendRequest(self, requestUserId: str) -> dict:
        response: dict = self.apiManager.acceptFriendRequest(requestUserId)
        return self._updateUserResources(response)

    def removeFriend(self, friendUserId: str) -> dict:
        response: dict = self.apiManager.removeFriend(friendUserId)
        return self._updateUserResources(response)
