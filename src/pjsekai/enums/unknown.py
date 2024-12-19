# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations
from typing import Any
from pydantic import RootModel, ConfigDict, model_validator


class Unknown(RootModel):
    _ignore_ = ["_raw_value"]
    root: str

    # @model_validator(mode='before')
    # @classmethod
    # def allow_unknown(cls, data: Any) -> Any:
    #     raise ValueError(f"{data}")

    @property
    def raw_value(self) -> str:
        return self.root

    @property
    def value(self) -> str:
        return self.root

    def __str__(self) -> str:
        return "%s: %s" % (super().__str__(), self.raw_value)

    def __repr__(self) -> str:
        return "<%s.UNKNOWN: '%s'>" % (self.__class__.__name__, self.raw_value)