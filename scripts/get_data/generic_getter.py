import requests
from os.path import basename
from os import makedirs
from os.path import join
import wget
def getter(urls, raw_folder):
    makedirs(raw_folder, exist_ok=True)
    for url in urls:
        path = join(raw_folder, basename(url))
        try:
            file = wget.download(url, path)
        except:
            print(url, "not found")