# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import List, Optional, Union, Dict

from pjsekai.enums import *
from .model import Model

class Bundle(Model):
    bundle_name: Optional[str]
    cache_directory_name: Optional[str]
    hash: Optional[str]
    category: Union[BundleCategory, Unknown, None]
    crc: Optional[int]
    file_size: Optional[int]
    dependencies: Optional[List[str]]
    paths: Optional[List[str]]
    is_builtin: Optional[bool]


class AssetBundleInfo(Model):
    version: Optional[str]
    os: Union[AssetOS, Unknown, None]
    bundles: Optional[Dict[str, Bundle]]
