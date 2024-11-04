# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Iterator
from math import ceil
from pathlib import Path
from struct import unpack
from typing import Optional

from msgpack import packb, unpackb
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from pjsekai.models import AppInfo

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

def read_app_info(apk_path: Path, version: str = "2022.3.32f1") -> AppInfo:
    try:
        import UnityPy  # type: ignore[import-untyped]
    except ImportError as e:
        raise ImportError("pip install pypjsekai[appinfo]") from e
    UnityPy.config.FALLBACK_UNITY_VERSION = version
    
    strings = []    
    env: UnityPy.Environment = UnityPy.load(str(apk_path))
    for obj in env.objects:
        if obj.type.name == "ResourceManager":
            data = obj.read()
            production_android_data = data.m_Container[
                "playersettings/android/production_android"].get_obj().read()
            i = 0
            while i<len(production_android_data.raw_data)-4:
                string_length, = unpack("<I",production_android_data.raw_data[i:i+4])
                i+=4
                string, = unpack(f"<{string_length}s",production_android_data.raw_data[i:i+string_length])
                i+=ceil(string_length/4)*4
                strings.append(string.decode("utf-8"))

    return AppInfo(**dict(zip(AppInfo.model_fields.keys(), strings)))