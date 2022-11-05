# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import Optional, Union

from pjsekai.enums import *
from .model import Model

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
    banner_asset_bundle_name: Optional[str]
    end_at: Optional[datetime]
