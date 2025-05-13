# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional

from pjsekai.enums import *
from .model import Model


class Bundle(Model):
    bundle_name: Optional[str] = None
    cache_directory_name: Optional[str] = None
    cache_file_name: Optional[str] = None
    hash: Optional[str] = None
    category: Optional[AllowUnknown[BundleCategory]] = None
    crc: Optional[int] = None
    file_size: Optional[int] = None
    dependencies: Optional[list[str]] = None
    paths: Optional[list[str]] = None
    is_builtin: Optional[bool] = None


class AssetBundleInfo(Model):
    version: Optional[str] = None
    os: Optional[AllowUnknown[AssetOS]] = None
    bundles: Optional[dict[str, Bundle]] = None
