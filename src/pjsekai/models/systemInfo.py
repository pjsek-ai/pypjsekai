# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional, Union

from .model import ModelWithExtra
from pjsekai.enums import *

class SystemInfo(ModelWithExtra):
    systemProfile: Optional[str]
    appVersion: Optional[str]
    multiPlayVersion: Optional[str]
    dataVersion: Optional[str]
    assetVersion: Optional[str]
    appHash: Optional[str]
    assetHash: Optional[str]
    appVersionStatus: Union[AppVersionStatus, Unknown, None]
