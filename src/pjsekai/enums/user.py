# SPDX-FileCopyrightText: 2024-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from enum import Enum

class CardSpecialTrainingStatus(Enum):
    DONE = "done"
    NOT_DOING = "not_doing"


class CardSpecialTrainingDisplayType(Enum):
    ORIGINAL = "original"
    SPECIAL_TRAINING = "special_training"


class ProfileImageType(Enum):
    LEADER = "leader"


class ProfileHonorType(Enum):
    NORMAL = "normal"
    BONDS = "bonds"


class BondsHonorViewType(Enum):
    NORMAL = "normal"
    REVERSE = "reverse"
    NONE = "none"