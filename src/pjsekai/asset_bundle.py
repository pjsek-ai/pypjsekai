# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, Iterator
from importlib.resources import as_file, files
from json import JSONDecodeError, dump, loads
from operator import attrgetter, itemgetter
from platform import system
from shutil import copyfileobj
from subprocess import PIPE, run
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, Any, Optional
from itertools import chain
from warnings import warn

from pjsekai.models import Bundle
from pjsekai.utilities import deobfuscated, obfuscated
from pathlib import Path

if TYPE_CHECKING:
    try:
        from UnityPy import Environment  # type: ignore[import-untyped]
        from UnityPy.files import ObjectReader  # type: ignore[import-untyped]
    except ImportError:
        pass


class AssetBundleResponse:

    _chunks: Iterator[bytes]
    _obfuscated_chunks: Iterator[bytes]

    @property
    def chunks(self) -> Iterator[bytes]:
        return self._chunks

    @property
    def obfuscated_chunks(self) -> Iterator[bytes]:
        return self._obfuscated_chunks

    def __init__(self, chunks: Optional[Iterator[bytes]] = None, obfuscated_chunks: Optional[Iterator[bytes]] = None):
        if chunks is not None and obfuscated_chunks is not None:
            self._chunks = chunks
            self._obfuscated_chunks = obfuscated_chunks
        elif chunks is None and obfuscated_chunks is not None:
            self._obfuscated_chunks = obfuscated_chunks
            self._chunks = deobfuscated(obfuscated_chunks)
        elif chunks is not None and obfuscated_chunks is None:
            self._chunks = chunks
            self._obfuscated_chunks = obfuscated(chunks)
        else:
            raise ValueError

    @staticmethod
    def detectObfuscation(chunks: Iterator[bytes]) -> AssetBundleResponse:
        cache = bytes()
        count = 0
        for chunk in chunks:
            cache += chunk
            count += len(chunk)
            if (count-4) >= 7:
                break
        index = cache.find(b"UnityFS")
        if index == -1:
            return AssetBundleResponse(obfuscated_chunks=chain([cache], chunks))
        else:
            return AssetBundleResponse(chunks=chain([cache[index:]], chunks))

    def save(self, path: Path, obfuscated: bool = False, info: Optional[Bundle] = None, on_bytes_saved: Optional[Callable[[int], Any]] = None) -> AssetBundle:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as file:
            for chunk in self.obfuscated_chunks if obfuscated else self.chunks:
                file.write(chunk)
                if on_bytes_saved is not None:
                    on_bytes_saved(len(chunk))
            return AssetBundle(path, info)


class AssetBundle:

    path: Path
    info: Optional[Bundle]

    def __init__(self, path: Path, info: Optional[Bundle] = None):
        self.path = path
        self.info = info

    def load(self, version: str = "2022.3.32f1") -> Environment:
        try:
            import UnityPy  # type: ignore[import-untyped]
            from UnityPy import config
        except ImportError as e:
            raise ImportError("pip install pypjsekai[assetbundle]") from e
        config.FALLBACK_UNITY_VERSION = version
        return UnityPy.load(str(self.path))

    @staticmethod
    def build_live2d_model(build_model_data: dict[str, Any], directory: Path) -> tuple[set[Path], set[Path]]:
        moc3_filename = f"{build_model_data.get('Moc3FileName', '')}"
        (directory / moc3_filename).replace((directory / moc3_filename).with_suffix(""))
        return set([(directory / moc3_filename).with_suffix("")]), set([directory / moc3_filename])

    @staticmethod
    def build_live2d_motion(build_motion_data: dict[str, Any], directory: Path) -> tuple[set[Path], set[Path]]:
        warn("Yet to be supported", RuntimeWarning, stacklevel=2)
        return (set(), set())

    @staticmethod
    def build_video(movie_bundle_build_data: dict[str, Any], directory: Path) -> tuple[set[Path], set[Path]]:
        try:
            from wannacri.usm import Usm # type: ignore[import-untyped]
            import ffmpeg  # type: ignore[import-untyped]
        except ImportError as e:
            raise ImportError(
                "pip install pypjsekai[assetbundle]") from e

        created: set[Path] = set()
        removed: set[Path] = set()
        movie_bundle_data_list = movie_bundle_build_data.get(
            "movieBundleDatas")
        if isinstance(movie_bundle_data_list, list) and len(movie_bundle_data_list) > 0:
            first_movie_bundle_data = movie_bundle_data_list[0]
            if isinstance(first_movie_bundle_data, dict):
                if len(movie_bundle_data_list) > 1:
                    usm_filename = f"{movie_bundle_data_list[0].get('usmFileName', '')}"[
                        :-14]
                    with (directory / usm_filename).with_suffix(".usm").open("wb") as usm_file:
                        for movie_bundle_data in sorted(movie_bundle_data_list, key=itemgetter("index")):
                            usm_part_filename = f"{movie_bundle_data.get('usmFileName', '')}"
                            with (directory / usm_part_filename).open("rb") as usm_part_file:
                                copyfileobj(usm_part_file, usm_file)
                            (directory / usm_part_filename).unlink()
                            removed.add(directory / usm_part_filename)
                else:
                    usm_part_filename = f"{movie_bundle_data_list[0].get('usmFileName', '')}"
                    usm_filename = usm_part_filename[:-10]
                    (directory / usm_part_filename).replace((directory /
                                                            usm_filename).with_suffix(".usm"))
                    removed.add(directory / usm_part_filename)
                created.add((directory / usm_filename).with_suffix(".usm"))

                with TemporaryDirectory() as temp_directory:
                    videos, audios = Usm.open((directory / usm_filename).with_suffix(".usm"), encoding="cp932") \
                        .demux(temp_directory)
                    audio_inputs = {Path(audio).name: ffmpeg.input(
                        audio).audio for audio in audios}
                    inputs = []
                    for video in videos:
                        inputs.append(ffmpeg.input(video).video)
                        inputs.append(audio_inputs.get(Path(video).name, ffmpeg.input(
                            "anullsrc=r=16000:cl=mono:d=1", f="lavfi")))
                    ffmpeg.concat(*inputs, v=1, a=1) \
                        .output(str((directory / usm_filename).with_suffix(".mp4")), vcodec="h264", acodec="aac") \
                        .run(overwrite_output=True, quiet=True)
                created.add((directory / usm_filename).with_suffix(".mp4"))
        return created, removed

    @staticmethod
    def build_audio(sound_bundle_build_data: dict[str, Any], directory: Path) -> tuple[set[Path], set[Path]]:
        created: set[Path] = set()
        removed: set[Path] = set()
        sound_bundle_data_list = sound_bundle_build_data.get("acbFiles")
        if isinstance(sound_bundle_data_list, list) and len(sound_bundle_data_list) > 0:
            first_sound_bundle_data = sound_bundle_data_list[0]
            if isinstance(first_sound_bundle_data, dict):
                acb_filename = f"{first_sound_bundle_data.get('cueSheetName', '')}"
                acb_file_path = (directory / acb_filename).with_suffix(".acb")
                if len(sound_bundle_data_list) > 1:
                    with acb_file_path.open("wb") as acb_file:
                        for sound_bundle_data in sorted(sound_bundle_data_list, key=itemgetter("spilitFileNum")):
                            acb_part_filename = f"{sound_bundle_data.get('assetBundleFileName', '')}"
                            with (directory / acb_part_filename).open("rb") as acb_part_file:
                                copyfileobj(acb_part_file, acb_file)
                            (directory / acb_part_filename).unlink()
                            removed.add(directory / acb_part_filename)
                else:
                    acb_part_filename = f"{sound_bundle_data_list[0].get('assetBundleFileName', '')}"
                    (directory / acb_part_filename).replace(acb_file_path)
                    removed.add(directory / acb_part_filename)
                created.add(acb_file_path)

                sys = system()
                vgmstream_subdirectory = None
                vgmstream_cli_executable = "vgmstream-cli"
                if sys == "Windows":
                    vgmstream_subdirectory = "bin/win64/vgmstream"
                    vgmstream_cli_executable = "vgmstream-cli.exe"
                elif sys == "Linux":
                    vgmstream_subdirectory = "bin/linux/vgmstream"
                elif sys == "Darwin":
                    vgmstream_subdirectory = "bin/darwin/vgmstream"
                if vgmstream_subdirectory is not None:
                    with as_file(files(__package__).joinpath(vgmstream_subdirectory)) as vgmstream_directory_path:
                        if (vgmstream_directory_path/vgmstream_cli_executable).is_file():
                            vgmstream_info_output = run([
                                (vgmstream_directory_path /
                                 vgmstream_cli_executable).absolute(),
                                "-mI",
                                "-S 0",
                                acb_file_path.absolute(),
                            ], check=True, stdout=PIPE, text=True).stdout
                            for line in vgmstream_info_output.split("\n"):
                                try:
                                    stream_info = loads(line).get("streamInfo")
                                    if (index := f"{stream_info.get('index', '')}") != "" and (name := f"{stream_info.get('name', '')}") != "":
                                        wav_filename = name.split(
                                            ";", maxsplit=1)[0]
                                        run([
                                            (vgmstream_directory_path /
                                             vgmstream_cli_executable).absolute(),
                                            "-o",
                                            (directory / wav_filename).with_suffix(".wav").absolute(),
                                            "-S",
                                            f"{index}",
                                            acb_file_path.absolute(),
                                        ], check=True, stdout=PIPE, text=True)
                                        created.add(
                                            (directory / wav_filename).with_suffix(".wav"))
                                except JSONDecodeError:
                                    pass
        return created, removed

    def extract(self, temp_directory=Path("temp"), relative_root=Path("assets/sekai/assetbundle/resources")) -> set[Path]:
        try:
            from UnityPy.enums import ClassIDType # type: ignore[import-untyped]
            from wannacri.usm import Usm # type: ignore[import-untyped]
            import ffmpeg  # type: ignore[import-untyped]
        except ImportError as e:
            raise ImportError("pip install pypjsekai[assetbundle]")

        env: Environment = self.load()

        containers: dict[Optional[str], list[ObjectReader]] = defaultdict(list)
        for object in sorted(env.objects, key=attrgetter("type")):
            containers[object.container].append(object)

        extracted_file_paths: set[Path] = set()
        for container_path, objects in containers.items():
            if container_path is not None:

                build_model_data_list: list[dict] = []
                build_motion_data_list: list[dict] = []
                movie_bundle_build_data_list: list[dict] = []
                sound_bundle_build_data_list: list[dict] = []

                relative_container_path = Path(
                    container_path).relative_to(relative_root)

                relative_extract_directory = relative_container_path.parent

                if len(objects) > 1:
                    relative_extract_directory = relative_extract_directory/relative_container_path.stem

                extract_directory = (
                    temp_directory / relative_extract_directory)
                extract_directory.mkdir(parents=True, exist_ok=True)

                for object in objects:
                    if object.type in [ClassIDType.Sprite, ClassIDType.Texture2D, ClassIDType.TextAsset, ClassIDType.MonoBehaviour, ClassIDType.AnimationClip]:
                        data = object.read()

                        if len(objects) > 1:
                            if data.m_Name is not None:
                                extract_filename = Path(f"{data.m_Name}")
                            else:
                                extract_filename = Path(f"{object.path_id}")
                            if extract_filename.suffix == "" and object.type in [ClassIDType.Texture2D, ClassIDType.Sprite]:
                                extract_filename = extract_filename.with_suffix(
                                    relative_container_path.suffix)
                        else:
                            extract_filename = Path(
                                relative_container_path.name)

                        extract_file_path = extract_directory / extract_filename
                        if extract_file_path in extracted_file_paths:
                            extract_file_path = (extract_file_path.parent / f"{extract_file_path.stem}_{object.path_id}").with_suffix(extract_file_path.suffix)

                        if object.type in [ClassIDType.Texture2D, ClassIDType.Sprite]:
                            data.image.save(extract_file_path)
                        elif object.type in [ClassIDType.TextAsset]:
                            with extract_file_path.open("wb") as file:
                                file.write(data.m_Script.encode(
                                    "utf-8", "surrogateescape"))
                        elif object.type in [ClassIDType.MonoBehaviour, ClassIDType.AnimationClip]:
                            typetree = object.read_typetree()
                            with extract_file_path.open("w") as file:
                                dump(typetree, file, ensure_ascii=False)
                            if data.m_Name == "BuildModelData":
                                build_model_data_list.append(typetree)
                            elif data.m_Name == "BuildMotionData":
                                build_motion_data_list.append(typetree)
                            elif data.m_Name == "MovieBundleBuildData":
                                movie_bundle_build_data_list.append(typetree)
                            elif data.m_Name == "SoundBundleBuildData":
                                sound_bundle_build_data_list.append(typetree)

                        extracted_file_paths.add(extract_file_path)

                for build_model_data in build_model_data_list:
                    created, removed = self.build_live2d_model(
                        build_model_data, extract_directory)
                    extracted_file_paths = (
                        extracted_file_paths | created) - removed
                for build_motion_data in build_motion_data_list:
                    created, removed = self.build_live2d_motion(
                        build_motion_data, extract_directory)
                    extracted_file_paths = (
                        extracted_file_paths | created) - removed
                for movie_bundle_build_data in movie_bundle_build_data_list:
                    created, removed = self.build_video(
                        movie_bundle_build_data, extract_directory)
                    extracted_file_paths = (
                        extracted_file_paths | created) - removed
                for sound_bundle_build_data in sound_bundle_build_data_list:
                    created, removed = self.build_audio(
                        sound_bundle_build_data, extract_directory)
                    extracted_file_paths = (
                        extracted_file_paths | created) - removed
        return extracted_file_paths
