#http://ncrna-pred.com/AMP_data_for_download.tar.xz
from os import makedirs
import wget
import gzip
import tarfile

raw_data = "../../raw_data/ensemble_amppred/"
makedirs(raw_data, exist_ok=True)
file = wget.download(
    "http://ncrna-pred.com/AMP_data_for_download.tar.xz",
    f"{raw_data}/AMP_data_for_download.tar.xz")

tar = tarfile.open(file, 'r:xz')
tar.extractall(raw_data)