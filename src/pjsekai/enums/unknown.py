# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Annotated, TYPE_CHECKING, TypeVar, Union
from pydantic import BeforeValidator,Field
if TYPE_CHECKING:
    from enum import Enum
else :
    from aenum import Enum
from aenum import extend_enum # type: ignore[import-untyped]

class Unknown(Enum):
    def __str__(self):
        return self.name

    @classmethod
    def _missing_(cls, value):
        try:
            extend_enum(cls, str(value).upper(), value)
        except TypeError:
            pass
        return cls[str(value).upper()]

    @classmethod
    def _validator(cls, value):
        return cls(value)

T = TypeVar('T')
AllowUnknown = Annotated[Union[T,Annotated[Unknown,BeforeValidator(Unknown._validator)]],Field(union_mode="left_to_right")]
