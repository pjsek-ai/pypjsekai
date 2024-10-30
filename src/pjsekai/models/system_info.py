# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional, Union

from pydantic import ConfigDict

from pjsekai.enums import *
from .model import Model,to_pjsekai_camel

class SystemInfo(Model):
    model_config = ConfigDict(extra="allow", alias_generator=to_pjsekai_camel, populate_by_name=True)

    system_profile: Optional[str] = None
    app_version: Optional[str] = None
    multi_play_version: Optional[str] = None
    data_version: Optional[str] = None
    asset_version: Optional[str] = None
    app_hash: Optional[str] = None
    asset_hash: Optional[str] = None
    app_version_status: Optional[Union[AppVersionStatus, Unknown]] = None
    suite_master_split_path: Optional[list[str]] = None