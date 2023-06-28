import requests
from os import makedirs
raw_folder = "../../raw_data/ampfun/"
makedirs(raw_folder, exist_ok=True)

filenames = ["stage1/train_pos.fasta", "stage1/test_pos.fasta",
             "stage2/parasitic/train_pos.fasta", "stage2/parasitic/test_pos.fasta",
             "stage2/viral/train_pos.fasta", "stage2/viral/test_pos.fasta",
             "stage2/mammalian/train_pos.fasta", "stage2/mammalian/test_pos.fasta",
             "stage2/fungal/train_pos.fasta", "stage2/fungal/test_pos.fasta",
             "stage2/gram_pos/train_pos.fasta", "stage2/gram_pos/test_pos.fasta",
             "stage2/gram_neg/train_pos.fasta", "stage2/gram_neg/test_pos.fasta"
             ]
for file in filenames:
    url = f"http://fdblab.csie.ncu.edu.tw/AMPfun/download/{file}"
    res = requests.get(url)
    with open(raw_folder + file.replace("/", "_"), mode="w", encoding="utf-8") as file:
        file.write(res.text)