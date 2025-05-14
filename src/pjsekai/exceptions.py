# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

# from typing import Optional

from json import dumps
from typing import Optional
from requests import Response

from pjsekai.enums.enums import AppVersionStatus
from pjsekai.enums.unknown import AllowUnknown

class ProjectSekaiException(Exception):
    pass

class ProjectSekaiAPIException(ProjectSekaiException):
    response: Optional[Response]
    unpacked: Optional[dict]
    
    def __init__(self, *args, response: Optional[Response] = None, unpacked: Optional[dict] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.response = response
        self.unpacked = unpacked

    def __str__(self) -> str:
        return dumps(self.unpacked,indent=2,ensure_ascii=False)

class UnpackException(ProjectSekaiAPIException):
    raw: Optional[bytes]

    def __init__(self, *args, raw: Optional[bytes] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.raw = raw

class ProjectSekaiClientException(ProjectSekaiException):
    pass

class NoAppVersionOrHash(ProjectSekaiClientException):
    pass

class NotAuthenticatedException(ProjectSekaiClientException):
    pass


class ServerInMaintenance(ProjectSekaiClientException):
    pass

class AppVersionUnavailable(ProjectSekaiClientException):
    pass

class SessionExpired(ProjectSekaiAPIException):
    pass


class UpdateRequired(ProjectSekaiAPIException):
    pass


class AppUpdateRequired(UpdateRequired):
    pass


class DataUpdateRequired(UpdateRequired):
    data_version: str
    multi_play_version: str
    app_version_status: AllowUnknown[AppVersionStatus]
    suite_master_split_path: list[str]

    def __init__(self, *args, data_version: str, multi_play_version: str, app_version_status: AllowUnknown[AppVersionStatus], suite_master_split_path: list[str], **kwargs):
        super().__init__(*args, **kwargs)
        self.data_version = data_version
        self.multi_play_version = multi_play_version
        self.app_version_status = app_version_status
        self.suite_master_split_path = suite_master_split_path

class AssetUpdateRequired(UpdateRequired):
    asset_version: str
    asset_hash: str

    def __init__(self, *args, asset_version: str, asset_hash: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.asset_version = asset_version
        self.asset_hash = asset_hash


class MultipleUpdatesRequired(AssetUpdateRequired, DataUpdateRequired):
    def __init__(self, *args, data_version: str, multi_play_version: str, app_version_status: AllowUnknown[AppVersionStatus], suite_master_split_path: list[str], asset_version: str, asset_hash: str, **kwargs):
        super(UpdateRequired, self).__init__(*args, **kwargs)
        self.data_version = data_version
        self.multi_play_version = multi_play_version
        self.app_version_status = app_version_status
        self.suite_master_split_path = suite_master_split_path
        self.asset_version = asset_version
        self.asset_hash = asset_hash


class MissingJWTScecret(ProjectSekaiClientException):
    pass


class TutorialEnded(ProjectSekaiClientException):
    pass


class LiveActive(ProjectSekaiClientException):
    pass


class LiveNotActive(ProjectSekaiClientException):
    pass


class LiveDead(ProjectSekaiClientException):
    pass


class LiveNotDead(ProjectSekaiClientException):
    pass
