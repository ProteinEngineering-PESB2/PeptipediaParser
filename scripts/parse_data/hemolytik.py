import pandas as pd
import os
from Bio import SeqIO
from functions import verify_sequences
dfs = []
raw_folder = "../../raw_data/hemolytik/"
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    a = pd.read_csv(path).rename(columns={"SEQUENCE": "sequence"})[["sequence"]]
    a["activity"] = file.replace(".csv", "").lower()
    dfs.append(a)
df = pd.concat(dfs)
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/hemolytik.csv", index=False)