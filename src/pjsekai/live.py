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
        def willCombo(self) -> bool:
            return self is self.PERFECT or self is self.GREAT
        @property
        def competitiveScore(self) -> int:
            if self is self.PERFECT:
                return 3
            elif self is self.GREAT:
                return 2
            elif self is self.GOOD:
                return 1
            else:
                return 0
class SoloLive:

    _musicId: int
    _musicDifficultyId: int
    _musicVocalId: int
    _deckId: int
    _boostCount: int
    _isAuto: bool
    _isActive: bool
    _liveId: Optional[str]
    _skills: List[dict]
    _cutins: List[dict]
    _score: int
    _competitiveScore: int
    _judgementCounts: Dict[Judgement,int]
    _combo: int
    _maxCombo: int
    _life: int
    _tapCount: int
    _continueCount: int

    @property
    def musicId(self) -> int:
        return self._musicId
    @property
    def musicDifficultyId(self) -> int:
        return self._musicDifficultyId
    @property
    def musicVocalId(self) -> int:
        return self._musicVocalId
    @property
    def deckId(self) -> int:
        return self._deckId
    @property
    def boostCount(self) -> int:
        return self._boostCount
    @property
    def isAuto(self) -> bool:
        return self._isAuto

    @property
    def isActive(self) -> bool:
        return self._isActive
    @property
    def liveId(self) -> Optional[str]:
        return self._liveId
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
    def competitiveScore(self) -> int:
        return self._competitiveScore
    @property
    def perfectCount(self) -> int:
        return self._judgementCounts[Judgement.PERFECT]
    @property
    def greatCount(self) -> int:
        return self._judgementCounts[Judgement.GREAT]
    @property
    def goodCount(self) -> int:
        return self._judgementCounts[Judgement.GOOD]
    @property
    def badCount(self) -> int:
        return self._judgementCounts[Judgement.BAD]
    @property
    def missCount(self) -> int:
        return self._judgementCounts[Judgement.MISS]
    @property
    def combo(self) -> int:
        return self._combo
    @property
    def maxCombo(self) -> int:
        return self._maxCombo
    @property
    def life(self) -> int:
        return self._life
    @property
    def tapCount(self) -> int:
        return self._tapCount
    @property
    def continueCount(self) -> int:
        return self._continueCount

    def __init__(self, musicId: int, musicDifficultyId: int, musicVocalId: int, deckId: int, boostCount: int = 0, isAuto: bool = False) -> None:
        self._musicId = musicId
        self._musicDifficultyId = musicDifficultyId
        self._musicVocalId = musicVocalId
        self._deckId = deckId
        self._boostCount = boostCount
        self._isAuto = isAuto

        self._liveId = None
        self._skills = []
        self._cutins = []
        self._score = 0
        self._competitiveScore = 0
        self._judgementCounts = {
            Judgement.PERFECT: 0,
            Judgement.GREAT: 0,
            Judgement.GOOD: 0,
            Judgement.BAD: 0,
            Judgement.MISS: 0,
        }
        self._combo = 0
        self._maxCombo = 0
        self._life = 1000
        self._tapCount = 0
        self._continueCount = 0

        self._isActive = False

    def start(self, userLiveId, skills, comboCutins) -> None:
        if self._isActive:
            raise LiveActive()
        self._liveId = userLiveId
        self._skills = skills
        self._cutins = comboCutins
        self._score = 0
        self._competitiveScore = 0
        self._judgementCounts = {
            Judgement.PERFECT: 0,
            Judgement.GREAT: 0,
            Judgement.GOOD: 0,
            Judgement.BAD: 0,
            Judgement.MISS: 0,
        }
        self._combo = 0
        self._maxCombo = 0
        self._life = 1000
        self._tapCount = 0
        self._continueCount = 0

        self._isActive = True
    
    def end(self) -> None:
        if not self._isActive:
            raise LiveNotActive()
        self._isActive = False

    def judge(self, judgement: Optional[Judgement] = None, isTap: bool = True, scoreChange: int = 0, lifeChange: int = 0) -> None:
        if not self._isActive:
            raise LiveNotActive()
        if self._life <= 0:
            raise LiveDead()
        if isTap:
            self._tapCount = self._tapCount + 1
        if judgement is not None:
            self._judgementCounts[judgement] = self._judgementCounts[judgement] + 1
            self._competitiveScore = self._competitiveScore + judgement.competitiveScore
            if judgement.willCombo:
                self._combo = self._combo + 1
                self._maxCombo = max(self._combo, self._maxCombo)
        self._score = self._score + scoreChange
        self._life = min(max(0,self._life + lifeChange),2000)

    def revive(self) -> None:
        if not self._isActive:
            raise LiveNotActive()
        if self._life > 0:
            raise LiveNotDead()
        self._continueCount = self._continueCount + 1
        self._life = 1000
