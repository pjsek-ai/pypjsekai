# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from contextlib import contextmanager
from typing import Dict, List, Optional, Union
from uuid import uuid4

from requests import Session, HTTPError
from jwt import encode as jwtEncode

from pjsekai.models import SystemInfo, GameVersion, AssetOS
from pjsekai.asset_bundle import AssetBundle
from pjsekai.exceptions import UpdateRequired, SessionExpired, MissingJWTScecret
from pjsekai.enums.tutorial_status import TutorialStatus
from pjsekai.enums.platform import Platform
from pjsekai.utilities import encrypt, decrypt, msgpack, unmsgpack

class API:

    platform: Platform
    domains: Dict[str, str]
    key: Optional[bytes]
    iv : Optional[bytes]
    jwt_secret: Optional[str]
    system_info: SystemInfo
    enable_encryption: Dict[str,bool]
    game_version: GameVersion
    server_number: Optional[int]

    _session: Session
    @property
    def session(self) -> Session:
        return self._session

    _session_token: Optional[str]

    _api_domain: str
    @property
    def api_domain(self) -> str:
        try:
            return self._api_domain.format(
                (self.game_version.profile or "") + ("" if self.server_number is None else f"{self.server_number:02}"),
            )
        except IndexError:
            return self._api_domain
    @api_domain.setter
    def api_domain(self, new_value):
        self._api_domain = new_value
    _asset_bundle_domain: str
    @property
    def asset_bundle_domain(self) -> str:
        try:
            return self._asset_bundle_domain.format(
                self.game_version.profile or "", 
                self.game_version.asset_bundle_host_hash or "",
            )
        except IndexError:
            return self._asset_bundle_domain
    @asset_bundle_domain.setter
    def asset_bundle_domain(self, new_value):
        self._asset_bundle_domain = new_value
    _asset_bundle_info_domain: str
    @property
    def asset_bundle_info_domain(self) -> str:
        try:
            return self._asset_bundle_info_domain.format(
                self.game_version.profile or "", 
                self.game_version.asset_bundle_host_hash or "",
            )
        except IndexError:
            return self._asset_bundle_info_domain
    @asset_bundle_info_domain.setter
    def asset_bundle_info_domain(self, new_value):
        self._asset_bundle_info_domain = new_value
    _game_version_domain: str
    @property
    def game_version_domain(self) -> str:
        try:
            return self._game_version_domain.format(
                self.game_version.profile or "",
            )
        except IndexError:
            return self._game_version_domain
    @game_version_domain.setter
    def game_version_domain(self, new_value):
        self._game_version_domain = new_value
    _signature_domain: str
    @property
    def signature_domain(self) -> str:
        try:
            return self._signature_domain.format(
                self.game_version.profile or "",
            )
        except IndexError:
            return self._signature_domain
    @signature_domain.setter
    def signature_domain(self, new_value):
        self._signature_domain = new_value

    enable_api_encryption: bool
    enable_asset_bundle_encryption: bool
    enable_asset_bundle_info_encryption: bool
    enable_game_version_encryption: bool
    enable_signature_encryption: bool

    DEFAULT_API_DOMAIN: str = "production-game-api.sekai.colorfulpalette.org"
    DEFAULT_ASSET_BUNDLE_DOMAIN: str = "{0}-{1}-assetbundle.sekai.colorfulpalette.org"
    DEFAULT_ASSET_BUNDLE_INFO_DOMAIN: str = "{0}-{1}-assetbundle-info.sekai.colorfulpalette.org"
    DEFAULT_GAME_VERSION_DOMAIN: str = "game-version.sekai.colorfulpalette.org"
    DEFAULT_SIGNATURE_DOMAIN: str =  "issue.sekai.colorfulpalette.org"

    DEFAULT_ENABLE_API_ENCRYPTION: bool = True
    DEFAULT_ENABLE_ASSET_BUNDLE_ENCRYPTION: bool = False
    DEFAULT_ENABLE_ASSET_BUNDLE_INFO_ENCRYPTION: bool = True
    DEFAULT_ENABLE_GAME_VERSION_ENCRYPTION: bool = True
    DEFAULT_ENABLE_SIGNATURE_ENCRYPTION: bool = True

    DEFAULT_CHUNK_SIZE: int = 1024 * 1024

    def __init__(
        self, 
        platform: Platform, 
        key: Optional[bytes], 
        iv: Optional[bytes], 
        jwt_secret: Optional[str], 
        system_info: Optional[SystemInfo],
        api_domain: str,
        asset_bundle_domain: str,
        asset_bundle_info_domain: str,
        game_version_domain: str,
        signature_domain: str,
        enable_api_encryption: bool,
        enable_asset_bundle_encryption: bool,
        enable_asset_bundle_info_encryption: bool,
        enable_game_version_encryption: bool,
        enable_signature_encryption: bool,
        server_number: Optional[int] = None,
    ) -> None:
        self.platform = platform
        self._session = Session()
        self.key = key
        self.iv = iv
        self.jwt_secret = jwt_secret
        self.system_info = SystemInfo()
        if system_info is not None:
            self.system_info = system_info
        self.api_domain = api_domain
        self._asset_bundle_domain = asset_bundle_domain
        self._asset_bundle_info_domain = asset_bundle_info_domain
        self._game_version_domain = game_version_domain
        self._signature_domain = signature_domain
        self.enable_api_encryption = enable_api_encryption
        self.enable_asset_bundle_encryption = enable_asset_bundle_encryption
        self.enable_asset_bundle_info_encryption = enable_asset_bundle_info_encryption
        self.enable_game_version_encryption = enable_game_version_encryption
        self.enable_signature_encryption = enable_signature_encryption
        self.server_number = server_number

        self._session_token = None
        self.game_version = GameVersion()

    def _pack(self, plaintext_dict: Optional[dict], enable_encryption: bool = True) -> bytes:
        plaintext: bytes = msgpack(plaintext_dict)
        return encrypt(plaintext, self.key or b"", self.iv or b"") if enable_encryption else plaintext

    def _unpack(self, ciphertext: bytes, enable_decryption: bool = True) -> dict:
        plaintext: bytes = decrypt(ciphertext, self.key or b"", self.iv or b"") if enable_decryption else ciphertext
        return unmsgpack(plaintext)

    def _generate_headers(self, system_info: Optional[SystemInfo] = None) -> dict:
        app_version: Optional[str]
        data_version: Optional[str]
        asset_version: Optional[str]
        if system_info is None:
            app_version = self.system_info.app_version
            data_version = self.system_info.data_version
            asset_version = self.system_info.asset_version
        else:
            app_version = system_info.app_version
            data_version = system_info.data_version
            asset_version = system_info.asset_version
        return {
            "Content-Type": "application/octet-stream",
            "Accept": "application/octet-stream",
            "X-App-Version": app_version,
            "X-Data-Version": data_version,
            "X-Asset-Version": asset_version,
            "X-Request-Id": str(uuid4()),
            "X-Unity-Version": self.platform.unity_version,
            
            **({} if self._session_token is None else {
                "X-Session-Token": self._session_token,
            }),
            **self.platform.headers,
        }

    def get_signed_cookie(
        self, 
        signature_domain: Optional[str] = None,
        enable_signature_encryption: Optional[bool] = None,
        system_info: Optional[SystemInfo] = None,
    ) -> str:
        if signature_domain is None:
            signature_domain = self.signature_domain
        if enable_signature_encryption is None:
            enable_signature_encryption = self.enable_signature_encryption
        url: str = f"https://{signature_domain}/api/signature"
        with self.session.post(
            url,
            headers=self._generate_headers(system_info),
            data=self._pack(None,enable_signature_encryption),
        ) as response:
            response.raise_for_status()
            return response.headers["Set-Cookie"]

    def get_game_version(
        self, 
        app_version: Optional[str] = None, 
        app_hash: Optional[str] = None, 
        game_version_domain: Optional[str] = None,
        enable_game_version_encryption: Optional[bool] = None,
        system_info: Optional[SystemInfo] = None,
    ) -> dict:
        if game_version_domain is None:
            game_version_domain = self.game_version_domain
        if enable_game_version_encryption is None:
            enable_game_version_encryption = self.enable_game_version_encryption
        if app_version is None:
            if system_info is None:
                app_version = self.system_info.app_version
            else:
                app_version = system_info.app_version
        if app_hash is None:
            if system_info is None:
                app_hash = self.system_info.app_hash
            else:
                app_hash = system_info.app_hash
        url: str = f"https://{game_version_domain}/{app_version}/{app_hash}"
        with self.session.get(
            url,
            headers=self._generate_headers(system_info),
        ) as response:
            response.raise_for_status()
            return self._unpack(response.content, enable_game_version_encryption)

    def get_asset_bundle_info(
        self, 
        asset_version: Optional[str] = None,
        asset_bundle_info_domain: Optional[str] = None,
        enable_asset_bundle_info_encryption: Optional[bool] = None,
        system_info: Optional[SystemInfo] = None,
    ) -> dict:
        if asset_bundle_info_domain is None:
            asset_bundle_info_domain = self.asset_bundle_info_domain
        if enable_asset_bundle_info_encryption is None:
            enable_asset_bundle_info_encryption = self.enable_asset_bundle_info_encryption
        if asset_version is None:
            if system_info is None:
                asset_version = self.system_info.asset_version
            else:
                asset_version = system_info.asset_version
        url: str = f"https://{asset_bundle_info_domain}/api/version/{asset_version}/os/{self.platform.asset_os.value}"
        with self.session.get(url,headers=self._generate_headers(system_info)) as response:
            try:
                response.raise_for_status()
            except HTTPError as e:
                if response.status_code == 426:
                    raise UpdateRequired from e
                elif response.status_code == 403:
                    raise SessionExpired from e
                else:
                    raise
            return self._unpack(response.content, enable_asset_bundle_info_encryption)

    @contextmanager
    def download_asset_bundle(
        self, 
        asset_bundle_name: str, 
        chunk_size: Optional[int] = None,
        asset_bundle_domain: Optional[str] = None,
        enable_asset_bundle_encryption: Optional[bool] = None,
        asset_version: Optional[str] = None,
        asset_hash: Optional[str] = None,
        os: AssetOS = AssetOS.ANDROID,
    ):
        if chunk_size is None:
            chunk_size = self.DEFAULT_CHUNK_SIZE
        if asset_bundle_domain is None:
            asset_bundle_domain = self.asset_bundle_domain
        if enable_asset_bundle_encryption is None:
            enable_asset_bundle_encryption = self.enable_asset_bundle_encryption
        if asset_version is None:
            asset_version = self.system_info.asset_version
        if asset_hash is None:
            asset_hash = self.system_info.asset_hash
        if asset_version is None or asset_hash is None:
            raise UpdateRequired
        url: str = f"https://{asset_bundle_domain}/{asset_version}/{asset_hash}/{os.value}/{asset_bundle_name}"
        if enable_asset_bundle_encryption:
            raise NotImplementedError
        response = self.session.get(url, stream=True)
        try:
            try:
                response.raise_for_status()
            except HTTPError as e:
                if response.status_code == 426:
                    raise UpdateRequired from e
                elif response.status_code == 403:
                    raise SessionExpired from e
                else:
                    raise
            yield AssetBundle(obfuscated_chunks=response.iter_content(chunk_size=chunk_size))
        finally:
            response.close()

    def request(
        self, 
        method: str, 
        path: str, 
        params: Optional[dict] = None, 
        data: Optional[dict] = None, 
        headers: Optional[dict] = None,
        api_domain: Optional[str] = None,
        enable_api_encryption: Optional[bool] = None,
        system_info: Optional[SystemInfo] = None,
    ) -> dict:
        if api_domain is None:
            api_domain = self.api_domain
        if enable_api_encryption is None:
            enable_api_encryption = self.enable_api_encryption
        url: str = f"https://{api_domain}/api/{path}"
        with self.session.request(
            method,
            url,
            headers={
                **self._generate_headers(system_info),
                **({} if headers is None else headers),
            },
            params=params,
            data=self._pack(data,enable_api_encryption) if data is not None or method.casefold()=="POST".casefold() else None
        ) as response:
            try:
                response.raise_for_status()
            except HTTPError as e:
                if response.status_code == 426:
                    raise UpdateRequired from e
                elif response.status_code == 403:
                    raise SessionExpired from e
                else:
                    raise
            self._session_token = response.headers.get("X-Session-Token", self._session_token)
            return self._unpack(response.content,enable_api_encryption)
    
    def ping(self) -> dict:
        return self.request("GET","")

    def get_system_info(self) -> dict:
        return self.request("GET", "system")
    
    def register(self) -> dict:
        return self.request("POST", "user", data = self.platform.info)

    def authenticate(self, user_id: Union[int, str], credential: str) -> dict:
        responseDict: dict = self.request("PUT", f"user/{user_id}/auth", data = { "credential": credential })
        self._session_token = responseDict["sessionToken"]
        return responseDict

    def get_master_data(self, data_version: Optional[str] = None) -> dict:
        if data_version is None:
            return self.request("GET", f"suite/master")
        else:
            return self.request("GET", f"suite/master", system_info=self.system_info.copy(update={"data_version":data_version}))

    def get_notices(self) -> dict:
        return self.request("GET", f"information")

    def get_user_data(self, user_id: Union[int, str], name: Optional[str] = None) -> dict:
        params = {
            "isForceAllReload": name is None,
            "name": name,
        }
        return self.request("GET", f"suite/user/{user_id}", params=params)
    
    def get_login_bonus(self, user_id: Union[int, str]) -> dict:
        return self.request("PUT", f"user/{user_id}/home/refresh", data = {
            "refreshableTypes":[
                "new_pending_friend_request",
                "login_bonus"
            ]
        })

    def get_profile(self, user_id: Union[int, str]) -> dict:
        return self.request("GET", f"user/{user_id}/profile")

    def set_tutorial_status(self, user_id: Union[int, str], tutorial_status: TutorialStatus) -> dict:
        return self.request("PATCH", f"user/{user_id}/tutorial", data = { "tutorialStatus": tutorial_status.value })

    def generate_transfer_code(self, user_id: Union[int, str], password: str) -> dict:
        return self.request("PUT", f"user/{user_id}/inherit", data = { "password": password })

    def checkTransferCode(self, transfer_code: str, password: str) -> dict:
        if self.jwt_secret is None:
            raise MissingJWTScecret
        token_payload = {
            "inheritId": transfer_code,
            "password": password
        }
        header = {
            "x-inherit-id-verify-token": jwtEncode(token_payload, self.jwt_secret, algorithm="HS256"),
        }
        params = {
            "isExecuteInherit": False,
        }
        return self.request("POST", f"inherit/user/{transfer_code}", params=params, headers=header)

    def generate_credential(self, transfer_code: str, password: str) -> dict:
        if self.jwt_secret is None:
            raise MissingJWTScecret
        token_payload = {
            "inheritId": transfer_code,
            "password": password
        }
        header = {
            "x-inherit-id-verify-token": jwtEncode(token_payload, self.jwt_secret, algorithm="HS256"),
        }
        params = {
            "isExecuteInherit": True,
        }
        return self.request("POST", f"inherit/user/{transfer_code}", params=params, headers=header)

    def gacha(self, user_id: Union[int, str], gacha_id: int, gacha_behavior_id: int) -> dict:
        return self.request("PUT", f"user/{user_id}/gacha/{gacha_id}/gachaBehaviorId/{gacha_behavior_id}")

    def receive_presents(self, user_id: Union[int, str], present_ids: List[str]) -> dict:
        return self.request("POST", f"user/{user_id}/present", data = {
            "presentIds": present_ids
        })

    def start_solo_live(
        self, 
        user_id: Union[int, str], 
        music_id: int, 
        music_difficulty_id: int, 
        music_vocal_id: int, 
        deck_id: int, 
        boost_count: int, 
        is_auto: bool
    ) -> dict:
        return self.request("POST", f"user/{user_id}/live", data = {
            "musicId": music_id,
            "musicDifficultyId": music_difficulty_id,
            "musicVocalId": music_vocal_id,
            "deckId": deck_id,
            "boostCount": boost_count,
            "isAuto": is_auto
        })

    def end_solo_live(
        self, 
        user_id: Union[int, str], 
        live_id:str, 
        score: int, 
        perfect_count: int, 
        great_count: int, 
        good_count: int, 
        bad_count: int, 
        miss_count: int, 
        max_combo: int, 
        life: int, 
        tap_count: int, 
        continue_count: int
    ) -> dict:
        return self.request("PUT", f"user/{user_id}/live/{live_id}", data = {
            "score": score,
            "perfectCount": perfect_count,
            "greatCount": great_count,
            "goodCount": good_count,
            "badCount": bad_count,
            "missCount": miss_count,
            "maxCombo": max_combo,
            "life": life,
            "tapCount": tap_count,
            "continueCount": continue_count
        })

    def get_event_rankings(
        self, 
        user_id: Union[int, str], 
        event_id: int, 
        target_user_id: Union[int, str, None] = None, 
        target_rank: Optional[int] = None, 
        higher_limit: Optional[int] = None, 
        lower_limit: Optional[int] = None
    ) -> dict:
        if target_user_id is None and target_rank is None:
            target_user_id = user_id
        params = {
            "targetUserId": target_user_id,
            "targetRank": target_rank,
            "higherLimit": higher_limit,
            "lowerLimit": lower_limit,
        }
        return self.request("GET", f"user/{user_id}/event/{event_id}/ranking", params=params)

    def get_event_teams_player_count(self, event_id: int) -> dict:
        return self.request("GET", f"cheerful-carnival-team-count/{event_id}")

    def get_event_teams_point(self, event_id: int) -> dict:
        return self.request("GET", f"cheerful-carnival-team-point/{event_id}")

    def get_rank_match_rankings(
        self, 
        user_id: Union[int, str], 
        rank_match_season_id: int, 
        target_user_id: Union[int, str, None] = None, 
        target_rank: Optional[int] = None, 
        higher_limit: Optional[int] = None, 
        lower_limit: Optional[int] = None
    ) -> dict:
        if target_user_id is None and target_rank is None:
            target_user_id = user_id
        params = {
            "targetUserId": target_user_id,
            "targetRank": target_rank,
            "higherLimit": higher_limit,
            "lowerLimit": lower_limit,
        }
        return self.request("GET", f"user/{user_id}/rank-match-season/{rank_match_season_id}/ranking", params=params)

    def get_room_invitations(self, user_id: Union[int, str]) -> dict:
        return self.request("GET", f"user/{user_id}/invitation")
    
    def send_friend_request(self, user_id: Union[int, str], target_user_id: Union[int, str], message: Optional[str] = None) -> dict:
        return self.request("POST", f"user/{user_id}/friend/{target_user_id}", data={
            "message": message, 
            "friendRequestSentLocation": "id_search",
        })

    def reject_friend_request(self, user_id: Union[int, str], request_user_id: Union[int, str]) -> dict:
        params = {
            "type": "reject_friend_request",
        }
        return self.request("DELETE", f"user/{user_id}/friend/{request_user_id}", params=params)

    def accept_friend_request(self, user_id: Union[int, str], request_user_id: Union[int, str]) -> dict:
        return self.request("PUT", f"user/{user_id}/friend/{request_user_id}")

    def remove_friend(self, user_id: Union[int, str], friend_user_id: Union[int, str]) -> dict:
        params = {
            "type": "release_friend",
        }
        return self.request("DELETE", f"user/{user_id}/friend/{friend_user_id}", params=params)
