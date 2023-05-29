from os import listdir
import pandas as pd
import os
from functions import verify_sequences
full_data = []
raw_folder = "../../raw_data/satpdb/"
dfs = []
for filename in listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    with open(path, encoding="utf-8", mode="r") as file:
        text = file.read()
    sequences = ["".join(a.split("\n")[1:]) for a in text.split(">")]
    df = pd.DataFrame()
    df["sequence"] = sequences
    df["activity"] = filename.replace(".fasta", "")
    dfs.append(df)
df = pd.concat(dfs)
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/satpdb.csv", index=False)