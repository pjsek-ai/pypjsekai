# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from enum import Enum

class InformationType(Enum):
    CONTENT = "content"
    NORMAL = "normal"
    BUG = "bug"

class InformationTag(Enum):
    UPDATE = "update"
    INFORMATION = "information"
    BUG = "bug"
    GACHA = "gacha"
    CAMPAIGN = "campaign"
    EVENT = "event"
    MUSIC = "music"

class BrowseType(Enum):
    EXTERNAL = "external"
    INTERNAL = "internal"

class InformationPlatform(Enum):
    ALL = "all"
    IOS = "iOS"
    Android = "Android"