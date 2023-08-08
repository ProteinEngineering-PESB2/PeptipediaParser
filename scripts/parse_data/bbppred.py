from os import listdir
from Bio import SeqIO
import pandas as pd
import os
from functions import verify_sequences
full_data = []
raw_folder = "../../raw_data/bbppred/BBPpred_datasets/"
dfs = []
for filename in listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    a = pd.DataFrame([[a.id.split("|")[1], str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["activity", "sequence"])
    a = a[a.activity == "1"]
    a["activity"] = "blood brain barrier penetrating"
    dfs.append(a)
df = pd.concat(dfs)
df = df[["sequence", "activity"]]
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/bbppred.csv", index=False)