import pandas as pd
from Bio import SeqIO
import os
from functions import verify_sequences

raw_folder = "../../raw_data/predneurop/"
sequences = []
for filename in os.listdir(raw_folder):
    sequences += [str(a.seq) for a in SeqIO.parse(f"{raw_folder}/{filename}", format="fasta")]

df = pd.DataFrame()
df["sequence"] = sequences
df["activity"] = "neuropeptide"
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/predneurop.csv", index=False)