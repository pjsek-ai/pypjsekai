# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Any
from pydantic import BaseModel, Extra
from pydantic.json import pydantic_encoder
from pydantic.utils import to_lower_camel

class Model(BaseModel):
    class Config:
        extra = Extra.allow
        alias_generator = to_lower_camel
        allow_population_by_field_name = True

    @classmethod
    def encoder(cls, obj: Any) -> Any:
        if isinstance(obj, Model):
            return obj.dict(by_alias=True)
        return pydantic_encoder(obj)