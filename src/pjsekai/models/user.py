# SPDX-FileCopyrightText: 2024-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional, Union

from pjsekai.enums import *
from .model import Model


class UserCard(Model):
    card_id: Optional[int] = None
    level: Optional[int] = None
    master_rank: Optional[int] = None
    special_training_status: Optional[Union[CardSpecialTrainingStatus, Unknown]] = None
    default_image: Optional[Union[CardSpecialTrainingDisplayType, Unknown]] = None


class UserProfile(Model):
    user_id: Optional[int] = None
    word: Optional[str] = None
    twitter_id: Optional[str] = None
    profile_image_type: Optional[Union[ProfileImageType, Unknown]] = None


class UserProfileHonor(Model):
    seq: Optional[int] = None
    profile_honor_type: Optional[Union[ProfileHonorType, Unknown]] = None
    honor_id: Optional[int] = None
    honor_level: Optional[int] = None
    bonds_honor_view_type: Optional[Union[BondsHonorViewType, Unknown]] = None
    bonds_honor_word_id: Optional[int] = None


class UserCheerfulCarnival(Model):
    pass


class UserHonorMission(Model):
    honor_mission_type: Optional[Union[HonorMissionType, Unknown]] = None
    progress: Optional[int] = None