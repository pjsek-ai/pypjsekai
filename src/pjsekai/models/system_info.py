# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional, Union

from pjsekai.enums import *
from .model import Model

class SystemInfo(Model):
    system_profile: Optional[str]
    app_version: Optional[str]
    multi_play_version: Optional[str]
    data_version: Optional[str]
    asset_version: Optional[str]
    app_hash: Optional[str]
    asset_hash: Optional[str]
    app_version_status: Union[AppVersionStatus, Unknown, None]
