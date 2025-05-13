# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import Optional

from pjsekai.enums import *
from .model import Model


class Information(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    display_order: Optional[int] = None
    information_type: Optional[AllowUnknown[InformationType]] = None
    information_tag: Optional[AllowUnknown[InformationTag]] = None
    browse_type: Optional[AllowUnknown[BrowseType]] = None
    platform: Optional[AllowUnknown[InformationPlatform]] = None
    title: Optional[str] = None
    path: Optional[str] = None
    start_at: Optional[datetime] = None
    banner_asset_bundle_name: Optional[str] = None
    end_at: Optional[datetime] = None
