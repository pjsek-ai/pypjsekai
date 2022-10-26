# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from pydantic import BaseModel, Extra

class ModelWithExtra(BaseModel):
    class Config:
        extra = Extra.allow