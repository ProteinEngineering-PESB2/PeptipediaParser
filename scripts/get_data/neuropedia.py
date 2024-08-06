from os import makedirs
import wget
raw_data = "../../raw_data/neuropedia/"
makedirs(raw_data, exist_ok=True)
file = wget.download(
    "http://proteomics.ucsd.edu/Software/NeuroPedia/Downloads/Database_NeuroPedia_063011.xls",
    f"{raw_data}/Database_NeuroPedia_063011.xls")
