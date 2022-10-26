# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from enum import Enum
from typing import Dict

class Platform(Enum):
    ANDROID = "Android"
    IOS = "iOS"

    @property
    def unityVersion(self) -> str:
        return "2020.3.32f1"
    @property
    def userAgent(self) -> str:
        return "UnityPlayer/2020.3.32f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)"

    @property
    def info(self) -> Dict[str, str]:
        info = {
            "platform": self.value
        }
        if self is Platform.ANDROID:
            info.update({
                "deviceModel": "",
                "operatingSystem": "Android OS 8.1.0 / API-27 (OPM7.181005.003/4984324)",
            })
        elif self is Platform.IOS:
            info.update({
                "deviceModel": "",
                "operatingSystem": "",
            })
        else:
            info.update({
                "platform": "",
                "deviceModel": "",
                "operatingSystem": "",
            })
        return info

    @property
    def headers(self) -> Dict[str, str]:
        headers = {
            "User-Agent": self.userAgent,
            "X-Platform": self.value,
        }
        if self is Platform.ANDROID:
            headers.update({
                "X-DeviceModel": "",
                "X-OperatingSystem": "Android OS 8.1.0 / API-27 (OPM7.181005.003/4984324)",
            })
        elif self is Platform.IOS:
            headers.update({
                "X-DeviceModel": "",
                "X-OperatingSystem": "",
            })
        else:
            headers.update({
                "X-Platform": "",
                "X-DeviceModel": "",
                "X-OperatingSystem": "",
            })
        return headers

    @property
    def assetOS(self) -> "AssetOS":
        return AssetOS(self.value.lower())

class AssetOS(Enum):
    ANDROID = "android"
    IOS = "ios"

    @property
    def platform(self) -> Platform:
        if self is AssetOS.ANDROID:
            return Platform.ANDROID
        elif self is Platform.IOS:
            return Platform.IOS
        else:
            return Platform(self.value.capitalize())