# SPDX-FileCopyrightText: 2024-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional

from .model import Model


class AppInfo(Model):
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
