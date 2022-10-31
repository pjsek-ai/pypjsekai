# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

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
    def __init__(self, appVersion: str, appHash: str, multiPlayVersion: str):
        self.appVersion = appVersion
        self.appHash = appHash
        self.multiPlayVersion = multiPlayVersion

class DataUpdateRequired(UpdateRequired):
    def __init__(self, dataVersion: str, appVersionStatus: str):
        self.dataVersion = dataVersion
        self.appVersionStatus = appVersionStatus

class AssetUpdateRequired(UpdateRequired):
    def __init__(self, assetVersion: str, assetHash: str):
        self.assetVersion = assetVersion
        self.assetHash = assetHash

class MultipleUpdatesRequired(UpdateRequired):
    def __init__(self, dataVersion: str, assetVersion: str, assetHash: str, appVersionStatus: str):
        self.dataVersion = dataVersion
        self.assetVersion = assetVersion
        self.assetHash = assetHash
        self.appVersionStatus = appVersionStatus

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