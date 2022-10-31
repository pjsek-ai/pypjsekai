# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Iterator, Optional, List
from msgpack import packb, unpackb
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def msgpack(dict: Optional[dict]) -> bytes:
    return b"" if dict is None else packb(dict) 

def unmsgpack(data: bytes) -> dict:
    return unpackb(data, strict_map_key=False) if len(data)>0 else None

def encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext: bytes = cipher.encrypt(pad(plaintext, 16))
    return ciphertext

def decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext: bytes = unpad(cipher.decrypt(ciphertext), 16)
    return plaintext

def deobfuscated(obfuscatedChunks: Iterator[List[bytes]]) -> Iterator:
    return (chunk if chunkIndex>0 else bytes([byte[0] if i>=128 or i%8>=5 else byte[0]^0xFF for i,byte in enumerate(chunk[4:])]) for chunkIndex, chunk in enumerate(obfuscatedChunks))

def obfuscated(chunks: Iterator[List[bytes]]) -> Iterator:
    return (chunk if chunkIndex>0 else bytes([0x10,0,0,0]+[byte[0] if i>=128 or i%8>=5 else byte[0]^0xFF for i,byte in enumerate(chunk)]) for chunkIndex, chunk in enumerate(chunks))
