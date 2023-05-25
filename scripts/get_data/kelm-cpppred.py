#sairam.people.iitgn.ac.in/Dataset.zip
from os import makedirs
import wget
raw_data = "../../raw_data/kelm-cpppred/"
makedirs(raw_data, exist_ok=True)
file = wget.download(
    "http://sairam.people.iitgn.ac.in/Dataset.zip",
    f"{raw_data}/Dataset.zip")


import zipfile
with zipfile.ZipFile(file, 'r') as zip_ref:
    zip_ref.extractall(raw_data)
