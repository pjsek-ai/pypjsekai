# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import Optional, Union

from pjsekai.enums import *
from .model import Model


class Information(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    display_order: Optional[int] = None
    information_type: Optional[Union[InformationType, Unknown]] = None
    information_tag: Optional[Union[InformationTag, Unknown]] = None
    browse_type: Optional[Union[BrowseType, Unknown]] = None
    platform: Optional[Union[InformationPlatform, Unknown]] = None
    title: Optional[str] = None
    path: Optional[str] = None
    start_at: Optional[datetime] = None
    banner_asset_bundle_name: Optional[str] = None
    end_at: Optional[datetime] = None
