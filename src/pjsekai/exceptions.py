# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional


class ProjectSekaiException(Exception):
    pass

class NotAuthenticatedException(ProjectSekaiException):
    pass

class ServerInMaintenance(ProjectSekaiException):
    pass

class NoAvailableVersions(ProjectSekaiException):
    pass

class SessionExpired(ProjectSekaiException):
    pass

class UpdateRequired(ProjectSekaiException):
    pass

class AppUpdateRequired(UpdateRequired):
    app_version: Optional[str]
    app_hash: Optional[str]
    multi_play_version: Optional[str]
    def __init__(self, app_version: Optional[str] = None, app_hash: Optional[str] = None, multi_play_version: Optional[str] = None):
        self.app_version = app_version
        self.app_hash = app_hash
        self.multi_play_version = multi_play_version

class DataUpdateRequired(UpdateRequired):
    data_version: str
    app_version_status: str
    def __init__(self, data_version: str, app_version_status: str):
        self.data_version = data_version
        self.app_version_status = app_version_status

class AssetUpdateRequired(UpdateRequired):
    asset_version: str 
    asset_hash: str
    def __init__(self, asset_version: str, asset_hash: str):
        self.asset_version = asset_version
        self.asset_hash = asset_hash

class MultipleUpdatesRequired(UpdateRequired):
    data_version: str
    asset_version: str
    asset_hash: str
    app_version_status: str
    def __init__(self, data_version: str, asset_version: str, asset_hash: str, app_version_status: str):
        self.data_version = data_version
        self.asset_version = asset_version
        self.asset_hash = asset_hash
        self.app_version_status = app_version_status

class MissingJWTScecret(ProjectSekaiException):
    pass

class TutorialEnded(ProjectSekaiException):
    pass

class LiveActive(ProjectSekaiException):
    pass

class LiveNotActive(ProjectSekaiException):
    pass

class LiveDead(ProjectSekaiException):
    pass

class LiveNotDead(ProjectSekaiException):
    pass