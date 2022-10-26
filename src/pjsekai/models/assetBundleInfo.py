# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import List, Optional, Union, Dict

from .model import ModelWithExtra
from pjsekai.enums import *


class Bundle(ModelWithExtra):
    bundleName: Optional[str]
    cacheDirectoryName: Optional[str]
    hash: Optional[str]
    category: Union[BundleCategory, Unknown, None]
    crc: Optional[int]
    fileSize: Optional[int]
    dependencies: Optional[List[str]]
    paths: Optional[List[str]]
    isBuiltin: Optional[bool]


class AssetBundleInfo(ModelWithExtra):
    version: Optional[str]
    os: Union[AssetOS, Unknown, None]
    bundles: Optional[Dict[str, Bundle]]
