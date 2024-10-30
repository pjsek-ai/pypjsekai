from pjsekai import Client
from pathlib import Path
from subprocess import run
from platform import system
import os

key = b""
iv = b""
app_version=""
app_hash=""
user_id = ""
credential = ""

asset_bundle_name = "scenario/movie/opening1"
asset_bundle_directory = Path("temp")/"assetBundles"
extracted_directory = Path("temp")/"extracted"

client = Client(
    key=key,
    iv=iv,
    app_version=app_version,
    app_hash=app_hash,
)

client.login(user_id, credential)

with client.download_asset_bundle(asset_bundle_name) as (asset_bundle_response, response):
    asset_bundle = asset_bundle_response.save(asset_bundle_directory/asset_bundle_name)
    extracted = asset_bundle.extract(extracted_directory)
    for path in extracted:
        if path.suffix == ".mp4":
            sys = system()
            if sys == "Windows":
                os.startfile(path)
            elif sys == "Linux":
                run(("xdg-open", path))
            elif sys == "Darwin":
                run(("open", path))
