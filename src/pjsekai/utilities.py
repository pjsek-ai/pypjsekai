# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Iterator, Optional, List
from msgpack import packb, unpackb
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(plaintextDict: Optional[dict], key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext: bytes = b"" if plaintextDict is None else packb(plaintextDict) 
    ciphertext: bytes = cipher.encrypt(pad(plaintext, 16))
    return ciphertext

def decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> dict:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext: bytes = unpad(cipher.decrypt(ciphertext), 16)
    plaintextDict: dict = unpackb(plaintext, strict_map_key=False) if len(plaintext)>0 else None
    return plaintextDict

def deobfuscated(obfuscatedChunks: Iterator[List[bytes]]) -> Iterator:
    return (chunk if chunkIndex>0 else bytes([byte[0] if i>=128 or i%8>=5 else byte[0]^0xFF for i,byte in enumerate(chunk[4:])]) for chunkIndex, chunk in enumerate(obfuscatedChunks))

def obfuscated(chunks: Iterator[List[bytes]]) -> Iterator:
    return (chunk if chunkIndex>0 else bytes([0x10,0,0,0]+[byte[0] if i>=128 or i%8>=5 else byte[0]^0xFF for i,byte in enumerate(chunk)]) for chunkIndex, chunk in enumerate(chunks))
