# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Iterator
from importlib.resources import files
from json import loads
from pathlib import Path
from typing import Optional

from msgpack import packb, unpackb
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from pjsekai.models import AndroidPlayerSettingConfig, IOSPlayerSettingConfig

def msgpack(dict: Optional[dict]) -> bytes:
    return b"" if dict is None else packb(dict) 

def unmsgpack(data: bytes) -> Optional[dict]:
    return unpackb(data, strict_map_key=False) if len(data)>0 else None

def encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext: bytes = cipher.encrypt(pad(plaintext, 16))
    return ciphertext

def decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext: bytes = unpad(cipher.decrypt(ciphertext), 16)
    return plaintext

def deobfuscated(obfuscated_chunks: Iterator[bytes]) -> Iterator[bytes]:
    count = 0
    for chunk in obfuscated_chunks:
        if (count-4)>=128:
            yield chunk
        else:
            yield bytes([
                int(byte) if (count+i-4)>=128 or (count+i-4)%8>=5 else 
                int(byte)^0xFF 
                    for i,byte in enumerate(chunk) if (count+i)>=4
            ])
        count+=len(chunk)

def obfuscated(chunks: Iterator[bytes]) -> Iterator[bytes]:
    count = 0
    for chunk in chunks:
        if count>=128:
            yield chunk
        else:
            yield bytes([0x10,0,0,0]+[
                int(byte) if (count+i)>=128 or (count+i)%8>=5 else 
                int(byte)^0xFF 
                    for i,byte in enumerate(chunk)
            ]) 
        count+=len(chunk)

def read_app_info(apk_path: Path, version: str = "2022.3.32f1") -> tuple[AndroidPlayerSettingConfig, IOSPlayerSettingConfig]:
    try:
        import UnityPy  # type: ignore[import-untyped]
        from UnityPy import config
        from UnityPy.files import ObjectReader
    except ImportError as e:
        raise ImportError("pip install pypjsekai[appinfo]") from e
    config.FALLBACK_UNITY_VERSION = version
    
    env = UnityPy.load(str(apk_path))
    resource_manager = next(object for object in env.objects if object.type.name == "ResourceManager")
    android_object: ObjectReader = next(object for path,object in resource_manager.read().m_Container if path == "playersettings/android/production_android").deref()
    ios_object: ObjectReader = next(object for path,object in resource_manager.read().m_Container if path == "playersettings/ios/production_ios").deref()

    android_nodes = [{**node,"m_ByteSize": 0, "m_Version":1} for node in loads(files(__package__).joinpath("data/AndroidPlayerSettingConfigTypeTree.json").read_text())]
    ios_nodes = [{**node,"m_ByteSize": 0, "m_Version":1} for node in loads(files(__package__).joinpath("data/IOSPlayerSettingConfigTypeTree.json").read_text())]

    android_player_setting_config = android_object.read_typetree(android_nodes,check_read=False)
    ios_player_setting_config = ios_object.read_typetree(ios_nodes,check_read=False)

    return AndroidPlayerSettingConfig(**android_player_setting_config), IOSPlayerSettingConfig(**ios_player_setting_config)
