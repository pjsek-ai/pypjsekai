from pjsekai import Client
from pathlib import Path
from subprocess import run
import os
import sys
from tempfile import TemporaryDirectory

key = b""
iv = b""
app_version=""
app_hash=""
user_id = ""
credential = ""

asset_bundle_name = "scenario/movie/opening1"

client = Client(
    key=key,
    iv=iv,
    app_version=app_version,
    app_hash=app_hash,
)

client.login(user_id, credential)

with client.download_asset_bundle(asset_bundle_name) as (asset_bundle_response, response), TemporaryDirectory() as temporary_directory:
    asset_bundle = asset_bundle_response.save(Path(temporary_directory)/"assetBundles"/asset_bundle_name)
    extracted = asset_bundle.extract(Path(temporary_directory)/"extracted")
    for path in extracted:
        if path.suffix == ".mp4":
            if sys.platform == "win32":
                os.startfile(path)
            elif sys.platform == "darwin":
                run(("open", path))
            else:
                run(("xdg-open", path))
