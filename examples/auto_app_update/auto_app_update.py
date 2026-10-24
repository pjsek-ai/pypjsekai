from shutil import copyfileobj
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from pathlib import Path

from pjsekai import Client
from pjsekai.enums import Platform
from pjsekai.utilities import read_app_info

key = b""
iv = b""

user_id = ""
credential = ""

def update_app(client: Client):
    if client.verbose:
        print("GET", "https://d.apkpure.com/b/XAPK/com.sega.pjsekai?version=latest")
    with client.api_manager.session.get(
        "https://d.apkpure.com/b/XAPK/com.sega.pjsekai?version=latest", 
        headers={"User-Agent":"_"}, 
        stream=True,
    ) as response, TemporaryDirectory() as temporary_directory:
        response.raise_for_status()
        temporary_file_path = Path(temporary_directory) / "com.sega.pjsekai.xapk"
        with temporary_file_path.open("wb") as temporary_file:
            copyfileobj(response.raw, temporary_file)
        with ZipFile(temporary_file_path, "r") as zip_file:
            zip_file.extractall(Path(temporary_directory)/"extracted")
        android, ios = read_app_info(Path(temporary_directory)/"extracted")
        if client.platform is Platform.ANDROID:
            return client.system_info.model_copy(update={
                "app_version": android.bundle_version,
                "app_hash": android.client_app_hash,
            })
        elif client.platform is Platform.IOS:
            return client.system_info.model_copy(update={
                "app_version": ios.bundle_version,
                "app_hash": ios.client_app_hash,
            })
        else:
            raise NotImplementedError("Unsupported platform")

client = Client(
    key=key,
    iv=iv,
    update_app=update_app
)

client.login(user_id, credential)

print(client.system_info)