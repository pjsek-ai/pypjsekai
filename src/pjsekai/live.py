# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from enum import Enum
from typing import Dict, List, Optional

from pjsekai.exceptions import LiveActive, LiveDead, LiveNotActive, LiveNotDead

class Judgement(Enum):
    PERFECT = "perfect"
    GREAT = "great"
    GOOD = "good"
    BAD = "bad"
    MISS = "miss"

    @property
    def will_combo(self) -> bool:
        return self is self.PERFECT or self is self.GREAT
    @property
    def competitive_score(self) -> int:
        if self is self.PERFECT:
            return 3
        elif self is self.GREAT:
            return 2
        elif self is self.GOOD:
            return 1
        else:
            return 0

class SoloLive:

    _music_id: int
    _music_difficulty_id: int
    _music_vocal_id: int
    _deck_id: int
    _boost_count: int
    _is_auto: bool
    _is_active: bool
    _live_id: Optional[str]
    _skills: List[dict]
    _cutins: List[dict]
    _score: int
    _competitive_score: int
    _judgement_counts: Dict[Judgement,int]
    _combo: int
    _max_combo: int
    _life: int
    _tap_count: int
    _continue_count: int

    @property
    def music_id(self) -> int:
        return self._music_id
    @property
    def music_difficulty_id(self) -> int:
        return self._music_difficulty_id
    @property
    def music_vocal_id(self) -> int:
        return self._music_vocal_id
    @property
    def deck_id(self) -> int:
        return self._deck_id
    @property
    def boost_count(self) -> int:
        return self._boost_count
    @property
    def is_auto(self) -> bool:
        return self._is_auto

    @property
    def is_active(self) -> bool:
        return self._is_active
    @property
    def live_id(self) -> Optional[str]:
        return self._live_id
    @property
    def skills(self) -> List[dict]:
        return self._skills
    @property
    def cutins(self) -> List[dict]:
        return self._cutins
    @property
    def score(self) -> int:
        return self._score
    @property
    def competitive_score(self) -> int:
        return self._competitive_score
    @property
    def perfect_count(self) -> int:
        return self._judgement_counts[Judgement.PERFECT]
    @property
    def great_count(self) -> int:
        return self._judgement_counts[Judgement.GREAT]
    @property
    def good_count(self) -> int:
        return self._judgement_counts[Judgement.GOOD]
    @property
    def bad_count(self) -> int:
        return self._judgement_counts[Judgement.BAD]
    @property
    def miss_count(self) -> int:
        return self._judgement_counts[Judgement.MISS]
    @property
    def combo(self) -> int:
        return self._combo
    @property
    def max_combo(self) -> int:
        return self._max_combo
    @property
    def life(self) -> int:
        return self._life
    @property
    def tap_count(self) -> int:
        return self._tap_count
    @property
    def continue_count(self) -> int:
        return self._continue_count

    def __init__(
        self,
        music_id: int,
        music_difficulty_id: int,
        music_vocal_id: int,
        deck_id: int,
        boost_count: int = 0,
        is_auto: bool = False,
    ) -> None:
        self._music_id = music_id
        self._music_difficulty_id = music_difficulty_id
        self._music_vocal_id = music_vocal_id
        self._deck_id = deck_id
        self._boost_count = boost_count
        self._is_auto = is_auto

        self._live_id = None
        self._skills = []
        self._cutins = []
        self._score = 0
        self._competitive_score = 0
        self._judgement_counts = {
            Judgement.PERFECT: 0,
            Judgement.GREAT: 0,
            Judgement.GOOD: 0,
            Judgement.BAD: 0,
            Judgement.MISS: 0,
        }
        self._combo = 0
        self._max_combo = 0
        self._life = 1000
        self._tap_count = 0
        self._continue_count = 0

        self._is_active = False

    def start(self, user_live_id, skills, combo_cutins) -> None:
        if self._is_active:
            raise LiveActive()
        self._live_id = user_live_id
        self._skills = skills
        self._cutins = combo_cutins
        self._score = 0
        self._competitive_score = 0
        self._judgement_counts = {
            Judgement.PERFECT: 0,
            Judgement.GREAT: 0,
            Judgement.GOOD: 0,
            Judgement.BAD: 0,
            Judgement.MISS: 0,
        }
        self._combo = 0
        self._max_combo = 0
        self._life = 1000
        self._tap_count = 0
        self._continue_count = 0

        self._is_active = True
    
    def end(self) -> None:
        if not self._is_active:
            raise LiveNotActive()
        self._is_active = False

    def judge(
        self, 
        judgement: Optional[Judgement] = None, 
        is_tap: bool = True, 
        score_change: int = 0, 
        life_change: int = 0,
    ) -> None:
        if not self._is_active:
            raise LiveNotActive()
        if self._life <= 0:
            raise LiveDead()
        if is_tap:
            self._tap_count = self._tap_count + 1
        if judgement is not None:
            self._judgement_counts[judgement] = self._judgement_counts[judgement] + 1
            self._competitive_score = self._competitive_score + judgement.competitive_score
            if judgement.will_combo:
                self._combo = self._combo + 1
                self._max_combo = max(self._combo, self._max_combo)
        self._score = self._score + score_change
        self._life = min(max(0,self._life + life_change),2000)

    def revive(self) -> None:
        if not self._is_active:
            raise LiveNotActive()
        if self._life > 0:
            raise LiveNotDead()
        self._continue_count = self._continue_count + 1
        self._life = 1000
