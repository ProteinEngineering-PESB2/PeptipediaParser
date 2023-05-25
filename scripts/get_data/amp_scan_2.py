from os import makedirs
import wget
from zipfile import ZipFile
raw_folder = "../../raw_data/amp_scan_2/"
makedirs(raw_folder, exist_ok=True)
file = wget.download(
    "https://www.dveltri.com/ascan/v2/data/AMP_Scan2_OrigPaper_Dataset.zip",
    f"{raw_folder}/AMP_Scan2_OrigPaper_Dataset.zip")
with ZipFile(file, 'r') as zObject:
    zObject.extractall(
        path=raw_folder)