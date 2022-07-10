import os
import shutil
import requests


def download_file(url, directory, fname=None):
    if fname==None:
        fname=os.path.basename(url)
    new_dl_path = os.path.join(directory, fname)
    with requests.get(url, stream=True) as r:
        with open(new_dl_path, "wb") as file_obj:
            shutil.copyfileobj(r.raw, file_obj)
    return new_dl_path