# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Any
from pydantic import ConfigDict, BaseModel
from pydantic.json import pydantic_encoder


def to_pjsekai_camel(string: str) -> str:
    return (string.split("_")[0]+"".join(word.capitalize() for word in string.split("_")[1:])) \
        .replace("AssetBundle", "Assetbundle") \
        .replace("assetBundle", "assetbundle")


class Model(BaseModel):
    model_config = ConfigDict(extra="allow", alias_generator=to_pjsekai_camel, populate_by_name=True, protected_namespaces=())

    @classmethod
    def encoder(cls, obj: Any) -> Any:
        if isinstance(obj, Model):
            return obj.model_dump(
                by_alias=True, 
                exclude_none=True, 
                exclude_unset=True, 
                serialize_as_any=True,
                round_trip=True
            )
        return pydantic_encoder(obj)


class Empty(Model):
    pass
