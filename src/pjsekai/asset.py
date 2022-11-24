# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional
from json import JSONDecodeError, dump, load
from pathlib import Path

from pjsekai.api import API
from pjsekai.models import AssetBundleInfo

class Asset:

    _path: Optional[Path]
    @property
    def path(self) -> Optional[Path]:
        return self._path
        
    _version: str
    @property
    def version(self) -> str:
        return self._version

    _hash: str
    @property
    def hash(self) -> str:
        return self._hash

    _asset_bundle_info: Optional[AssetBundleInfo]
    @property
    def asset_bundle_info(self) -> Optional[AssetBundleInfo]:
        return self._asset_bundle_info
    @asset_bundle_info.setter
    def asset_bundle_info(self, new_value: Optional[AssetBundleInfo]) -> None:
        self._asset_bundle_info = new_value
        if self.path is not None and new_value is not None:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.joinpath("AssetBundleInfo.json").open("w") as f:
                dump(new_value,f,indent=2,ensure_ascii=False,default=AssetBundleInfo.encoder)

    def __init__(self, version: str, hash: str, asset_directory: Optional[str] = None) -> None:
        if asset_directory is not None:
            p = Path(asset_directory)
            if p.exists and not p.is_dir():
                raise NotADirectoryError
            self._path = p

        self._version = version
        self._hash = hash

        if self.path is not None:
            try:
                with self.path.joinpath("AssetBundleInfo.json").open("r") as f:
                    self._asset_bundle_info = AssetBundleInfo(**load(f))
            except (FileNotFoundError, JSONDecodeError):
                self.asset_bundle_info = None
        else:
            self.asset_bundle_info = None

    def get_asset_bundle_info(self, api_manager: API) -> AssetBundleInfo:
        self.asset_bundle_info = AssetBundleInfo(**api_manager.get_asset_bundle_info(self._version))
        return self.asset_bundle_info
