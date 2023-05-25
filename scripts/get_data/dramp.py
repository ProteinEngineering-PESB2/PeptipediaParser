from os.path import basename
import requests
from os import makedirs
url = "http://dramp.cpu-bioinfor.org/downloads/download.php?filename=download_data/DRAMP3.0_new/general_amps.xlsx"
raw_folder = "../../raw_data/dramp/"
makedirs(raw_folder)
path = raw_folder + basename(url)
with open(path, encoding="utf-8", mode="w") as file:
    file.write(requests.get(url).text)