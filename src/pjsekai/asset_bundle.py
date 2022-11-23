# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Iterator, Optional

from pjsekai.utilities import deobfuscated, obfuscated

class AssetBundle:

    _chunks: Iterator[bytes]
    _obfuscated_chunks: Iterator[bytes]
    
    @property
    def chunks(self) -> Iterator[bytes]:
        return self._chunks
    @property
    def obfuscated_chunks(self) -> Iterator[bytes]:
        return self._obfuscated_chunks

    def __init__(self, chunks: Optional[Iterator[bytes]] = None, obfuscated_chunks: Optional[Iterator[bytes]] = None):
        if chunks is not None:
            self._chunks = chunks
            self._obfuscated_chunks = obfuscated(chunks)
        elif obfuscated_chunks is not None:
            self._chunks = deobfuscated(obfuscated_chunks)
            self._obfuscated_chunks = obfuscated_chunks
        else:
            raise ValueError
            
    def extract(self) -> None:
        raise NotImplementedError
