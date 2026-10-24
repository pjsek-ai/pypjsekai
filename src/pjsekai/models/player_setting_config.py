# SPDX-FileCopyrightText: 2024-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional

from pydantic import ConfigDict

from .model import Model, to_pjsekai_camel


class PlayerSettingConfig(Model):
    model_config = ConfigDict(extra="ignore", alias_generator=to_pjsekai_camel, populate_by_name=True, protected_namespaces=())

    memo: Optional[str] = None
    client_major_version: Optional[str] = None
    client_minor_version: Optional[str] = None
    client_build_version: Optional[str] = None
    snapshot: Optional[str] = None
    client_version_suffix: Optional[str] = None
    client_data_major_version: Optional[str] = None
    client_data_minor_version: Optional[str] = None
    client_data_build_version: Optional[str] = None
    client_data_revision: Optional[str] = None
    company_name: Optional[str] = None
    product_name: Optional[str] = None
    bundle_identifier: Optional[str] = None
    bundle_version: Optional[str] = None
    asset_hash: Optional[str] = None
    client_app_hash: Optional[str] = None
    ad_mob_app_id: Optional[str] = None


class AndroidPlayerSettingConfig(PlayerSettingConfig):
    bundle_version_code: Optional[int] = None


class IOSPlayerSettingConfig(PlayerSettingConfig):
    application_display_name: Optional[str] = None
    build_number: Optional[str] = None