# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import Optional, Union

from .model import Model
from pjsekai.enums import *

class Information(Model):
    id: Optional[int]
    seq: Optional[int]
    display_order: Optional[int]
    information_type: Union[InformationType, Unknown, None]
    information_tag: Union[InformationTag, Unknown, None]
    browse_type: Union[BrowseType, Unknown, None]
    platform: Union[InformationPlatform, Unknown, None]
    title: Optional[str]
    path: Optional[str]
    start_at: Optional[datetime]
    banner_assetbundle_name: Optional[str]
    end_at: Optional[datetime]
