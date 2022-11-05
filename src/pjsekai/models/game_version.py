# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional
from pydantic import Field

from .model import Model
from pjsekai.enums import *

class GameVersion(Model):
    profile: Optional[str]
    asset_bundle_host_hash: Optional[str] = Field(aliases=["assetbundleHostHash"])
    domain: Optional[str]