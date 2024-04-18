# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import List, Optional, Union, Dict

from pjsekai.enums import *
from .model import Model


class Bundle(Model):
    bundle_name: Optional[str] = None
    cache_directory_name: Optional[str] = None
    cache_file_name: Optional[str] = None
    hash: Optional[str] = None
    category: Optional[Union[BundleCategory, Unknown]] = None
    crc: Optional[int] = None
    file_size: Optional[int] = None
    dependencies: Optional[List[str]] = None
    paths: Optional[List[str]] = None
    is_builtin: Optional[bool] = None


class AssetBundleInfo(Model):
    version: Optional[str] = None
    os: Optional[Union[AssetOS, Unknown]] = None
    bundles: Optional[Dict[str, Bundle]] = None
