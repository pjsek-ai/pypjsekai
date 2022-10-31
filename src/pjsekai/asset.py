# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional
from json import JSONDecodeError, dump, load
from os import path, makedirs
from pydantic.json import pydantic_encoder

from pjsekai.api import API
from pjsekai.models import *

class Asset:

    _path: Optional[str]
    _version: str
    _hash: str
    _assetBundleInfo: Optional[AssetBundleInfo]

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
    def assetBundleInfo(self) -> Optional[AssetBundleInfo]:
        return self._assetBundleInfo
    @assetBundleInfo.setter
    def assetBundleInfo(self, newValue: Optional[AssetBundleInfo]) -> None:
        self._assetBundleInfo = newValue
        if self._path is not None and newValue is not None:
            makedirs(self._path,exist_ok=True)
            with open(path.join(self._path,"AssetBundleInfo.json"), "w") as f:
                dump(newValue,f,indent=2,ensure_ascii=False,default=pydantic_encoder)

    def __init__(self, version: str, hash: str, assetsPath: Optional[str] = None) -> None:
        self._path = assetsPath

        self._version = version
        self._hash = hash

        if self._path is not None:
            try:
                with open(path.join(self._path,"AssetBundleInfo.json"), "r") as f:
                    self._assetBundleInfo = AssetBundleInfo(**load(f))
            except (FileNotFoundError, JSONDecodeError):
                self.assetBundleInfo = None
        else:
            self.assetBundleInfo = None

    def getAssetBundleInfo(self, apiManager: API) -> AssetBundleInfo:
        self.assetBundleInfo = AssetBundleInfo(**apiManager.getAssetBundleInfo(self._version))
        return self.assetBundleInfo
