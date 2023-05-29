import pandas as pd
import os
from Bio import SeqIO
from functions import verify_sequences
dfs = []
raw_folder = "../../raw_data/erop_moskow/"
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
    a["activity"] = file.replace(".fasta", "").lower()
    dfs.append(a)
df = pd.concat(dfs)
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/erop_moskow.csv", index=False)