import os
from Bio import SeqIO
import pandas as pd
from functions import verify_sequences
path = "../../raw_data/kelm-cpppred/Dataset/Independent-dataset/pos.fasta"
df = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
df["activity"] = "cell penetrating"
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/kelm-cpppred.csv", index=False)