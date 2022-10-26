# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Iterator, List, Optional

from pjsekai.utilities import deobfuscated, obfuscated

class AssetBundle:

    _chunks: Iterator[List[bytes]]
    _obfuscatedChunks: Iterator[List[bytes]]
    
    @property
    def chunks(self) -> Iterator[List[bytes]]:
        return self._chunks
    @property
    def obfuscatedChunks(self) -> Iterator[List[bytes]]:
        return self._obfuscatedChunks

    def __init__(self, chunks: Optional[Iterator[List[bytes]]] = None, obfuscatedChunks: Optional[Iterator[List[bytes]]] = None):
        if chunks is not None:
            self._chunks = chunks
            self._obfuscatedChunks = obfuscated(chunks)
        elif obfuscatedChunks is not None:
            self._chunks = deobfuscated(obfuscatedChunks)
            self._obfuscatedChunks = obfuscatedChunks
        else:
            raise ValueError
            
    def extract(self) -> None:
        raise NotImplementedError
