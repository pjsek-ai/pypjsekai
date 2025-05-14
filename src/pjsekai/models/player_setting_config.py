# SPDX-FileCopyrightText: 2024-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional

from pydantic import ConfigDict

from .model import Model, to_pjsekai_camel


class PlayerSettingConfig(Model):
    model_config = ConfigDict(extra="ignore", alias_generator=to_pjsekai_camel, populate_by_name=True, protected_namespaces=())

    memo: Optional[str] = None
    clientMajorVersion: Optional[str] = None
    clientMinorVersion: Optional[str] = None
    clientBuildVersion: Optional[str] = None
    snapshot: Optional[str] = None
    clientVersionSuffix: Optional[str] = None
    clientDataMajorVersion: Optional[str] = None
    clientDataMinorVersion: Optional[str] = None
    clientDataBuildVersion: Optional[str] = None
    clientDataRevision: Optional[str] = None
    companyName: Optional[str] = None
    productName: Optional[str] = None
    bundleIdentifier: Optional[str] = None
    bundleVersion: Optional[str] = None
    assetHash: Optional[str] = None
    clientAppHash: Optional[str] = None
    adMobAppId: Optional[str] = None


class AndroidPlayerSettingConfig(PlayerSettingConfig):
    bundleVersionCode: Optional[int] = None


class IOSPlayerSettingConfig(PlayerSettingConfig):
    applicationDisplayName: Optional[str] = None
    buildNumber: Optional[str] = None