import os
import pandas as pd
from Bio import SeqIO
from functions import verify_sequences
raw_folder = "../../raw_data/ennavia"
dfs = []
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    a = pd.DataFrame([[str(a.seq), a.id.split("|")[3]] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence", "activity"])
    a = a[~a.activity.str.contains("non")]
    dfs.append(a)
df = pd.concat(dfs)
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/ennavia.csv", index=False)