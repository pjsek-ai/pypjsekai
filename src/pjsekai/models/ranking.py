# SPDX-FileCopyrightText: 2024-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import Optional

from pjsekai.enums import *
from .user import *
from .model import Model


class Ranking(Model):
    user_id: Optional[int] = None
    score: Optional[int] = None
    rank: Optional[int] = None
    is_own: Optional[bool] = None
    name: Optional[str] = None
    user_card: Optional[UserCard] = None
    user_profile: Optional[UserProfile] = None
    user_profile_honors: Optional[list[UserProfileHonor]] = None
    user_cheerful_carnival: Optional[UserCheerfulCarnival] = None
    user_honor_missions: Optional[list[UserHonorMission]] = None


class WorldBloomChapterRanking(Model):
    event_id: Optional[int] = None
    game_character_id: Optional[int] = None
    rankings: Optional[list[Ranking]] = None
    user_ranking_status: Optional[AllowUnknown[UserRankingStatus]] = None
    is_world_bloom_chapter_aggregate: Optional[bool] = None


class Rankings(Model):
    rankings: Optional[list[Ranking]] = None
    user_ranking_status: Optional[AllowUnknown[UserRankingStatus]] = None
    is_event_aggregate: Optional[bool] = None
    user_world_bloom_chapter_rankings: Optional[list[WorldBloomChapterRanking]] = None


class BorderRankings(Model):
    event_id: Optional[int] = None
    border_rankings: Optional[list[Ranking]] = None
    is_event_aggregate: Optional[bool] = None
    user_world_bloom_chapter_ranking_borders: Optional[list[WorldBloomChapterRanking]] = None


class UserRankMatchSeason(Model):
    rank_match_season_id: Optional[int] = None
    rank_match_tier_id: Optional[int] = None
    tier_point: Optional[int] = None
    total_tier_point: Optional[int] = None
    play_count: Optional[int] = None
    consecutive_win_count: Optional[int] = None
    max_consecutive_win_count: Optional[int] = None 
    win_count: Optional[int] = None
    lose_count: Optional[int] = None
    draw_count: Optional[int] = None
    penalty_count: Optional[int] = None
    playable_at: Optional[datetime] = None


class RankMatchRanking(Ranking):
    user_rank_match_season: Optional[UserRankMatchSeason] = None


class RankMatchRankings(Model):
    rankings: Optional[list[RankMatchRanking]] = None