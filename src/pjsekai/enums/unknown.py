# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from enum import Enum
from typing import Any, Optional

class Unknown(Enum):
    _UNKNOWN = "_unknown"

    _ignore_ = ["_rawValue"]

    _rawValue: Optional[Any]
    @property
    def rawValue(self):
        return self._rawValue
    @property
    def value(self):
        return self._rawValue

    def __init__(self, value: Optional[Any]):
        self._rawValue = value

    @classmethod
    def _missing_(cls, value: Optional[Any]):
        unknown = cls._UNKNOWN
        unknown._rawValue = value
        return unknown

    def __str__(self) -> str:
        return "%s: %s" % (super().__str__(), self.rawValue)

    def __repr__(self):
        return "<%s.%s: '%s'>" % (self.__class__.__name__, self.name, self.rawValue)
