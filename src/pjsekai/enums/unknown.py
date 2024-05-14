# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from enum import Enum
from typing import Any, Optional

class Unknown(Enum):
    _UNKNOWN = "_unknown"

    _ignore_ = ["_raw_value"]

    _raw_value: Optional[Any]

    @property
    def raw_value(self) -> Optional[Any]:
        return self._raw_value

    @property
    def value(self) -> Optional[Any]:
        return self._raw_value

    def __init__(self, value: Optional[Any]):
        self._raw_value = value

    @classmethod
    def _missing_(cls, value: Optional[Any]) -> Unknown:
        unknown = cls._UNKNOWN
        unknown._raw_value = value
        return unknown

    def __str__(self) -> str:
        return "%s: %s" % (super().__str__(), self.raw_value)

    def __repr__(self) -> str:
        return "<%s.%s: '%s'>" % (self.__class__.__name__, self.name, self.raw_value)
