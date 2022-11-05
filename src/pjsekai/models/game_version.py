# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional
from pydantic import Field

from pjsekai.enums import *
from .model import Model

class GameVersion(Model):
    profile: Optional[str]
    asset_bundle_host_hash: Optional[str]
    domain: Optional[str]