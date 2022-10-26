# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from enum import Enum

from pjsekai.exceptions import TutorialEnded
from pjsekai.enums.enums import Unit

class TutorialStatus(Enum):
    START = "start"
    OPENING_1 = "opening_1"
    GAMEPLAY = "gameplay"
    OPENING_2 = "opening_2"
    UNIT_SELECT = "unit_select"
    LN_OPENING = "light_sound_opening"
    MMJ_OPENING = "idol_opening"
    VBS_OPENING = "street_opening"
    WXS_OPENING = "theme_park_opening"
    NIIGO_OPENING = "school_refusal_opening"
    SUMMARY = "summary"
    END = "end"

    def next(self, unit: Unit = Unit.LN) -> "TutorialStatus":
        if self is TutorialStatus.START:
            return TutorialStatus.OPENING_1
        elif self is TutorialStatus.OPENING_1:
            return TutorialStatus.GAMEPLAY
        elif self is TutorialStatus.GAMEPLAY:
            return TutorialStatus.OPENING_2
        elif self is TutorialStatus.OPENING_2:
            return TutorialStatus.UNIT_SELECT
        elif self is TutorialStatus.UNIT_SELECT:
            return TutorialStatus(unit.value+"_opening")
        elif self is TutorialStatus.LN_OPENING or self is TutorialStatus.MMJ_OPENING or self is TutorialStatus.VBS_OPENING or self is TutorialStatus.WXS_OPENING or self is TutorialStatus.NIIGO_OPENING:
            return TutorialStatus.SUMMARY
        elif self is TutorialStatus.SUMMARY:
            return TutorialStatus.END
        else:
            raise TutorialEnded