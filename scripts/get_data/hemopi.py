import requests
from os.path import join
from os import makedirs
raw_folder = "../../raw_data/hemopi/"
makedirs(raw_folder, exist_ok=True)

filenames = ["HemoPI_1_dataset/main/pos.fa", "HemoPI_1_dataset/validation/pos.fa",
             "HemoPI_2_dataset/main/pos.fa", "HemoPI_2_dataset/validation/pos.fa",
             "HemoPI_3_dataset/main/pos.fa", "HemoPI_3_dataset/validation/pos.fa" ]

urls = [f"https://webs.iiitd.edu.in/raghava/hemopi/data/{filename}" for filename in filenames]

for filename, url in zip(filenames, urls):
    path = join(raw_folder, filename.replace("/", "_"))
    with open(path, encoding="utf-8", mode="w") as file:
        file.write(requests.get(url).text)
