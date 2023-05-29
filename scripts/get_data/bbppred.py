from generic_getter import getter
from zipfile import ZipFile
import os
raw_folder = "../../raw_data/bbpred/"
urls = ["http://bbppred.xialab.info/static/datasets/BBPpred_datasets.zip"]
getter(urls, raw_folder = raw_folder)
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
with ZipFile(path, 'r') as zObject:
    zObject.extractall(
        path=raw_folder)