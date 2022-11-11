# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional
from json import JSONDecodeError, dump, load
from os import path, makedirs

from pjsekai.api import API
from pjsekai.models import *

class Asset:

    _path: Optional[str]
    _version: str
    _hash: str
    _asset_bundle_info: Optional[AssetBundleInfo]

    @property
    def path(self) -> Optional[str]:
        return self._path
    @property
    def version(self) -> str:
        return self._version
    @property
    def hash(self) -> str:
        return self._hash
    @property
    def asset_bundle_info(self) -> Optional[AssetBundleInfo]:
        return self._asset_bundle_info
    @asset_bundle_info.setter
    def asset_bundle_info(self, new_value: Optional[AssetBundleInfo]) -> None:
        self._asset_bundle_info = new_value
        if self._path is not None and new_value is not None:
            makedirs(self._path,exist_ok=True)
            with open(path.join(self._path,"AssetBundleInfo.json"), "w") as f:
                dump(new_value,f,indent=2,ensure_ascii=False,default=AssetBundleInfo.encoder)

    def __init__(self, version: str, hash: str, assetsPath: Optional[str] = None) -> None:
        self._path = assetsPath

        self._version = version
        self._hash = hash

        if self._path is not None:
            try:
                with open(path.join(self._path,"AssetBundleInfo.json"), "r") as f:
                    self._asset_bundle_info = AssetBundleInfo(**load(f))
            except (FileNotFoundError, JSONDecodeError):
                self.asset_bundle_info = None
        else:
            self.asset_bundle_info = None

    def get_asset_bundle_info(self, api_manager: API) -> AssetBundleInfo:
        self.asset_bundle_info = AssetBundleInfo(**api_manager.get_asset_bundle_info(self._version))
        return self.asset_bundle_info
