import pandas as pd
from Bio import SeqIO
from functions import verify_sequences
import os


raw_folder = "../../raw_data/ensemble_amppred/AMP_data_for_download/"
sequences = []
for filename in os.listdir(raw_folder):
    if "AMP" in filename and "Non" not in filename:
        print(filename)
        sequences += [str(a.seq) for a in SeqIO.parse(f"{raw_folder}/{filename}", format="fasta")]

df = pd.DataFrame()
df["sequence"] = sequences
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df["activity"] = "antimicrobial"
print(df)
df.to_csv("../../parsed_data/ensemble_amppred.csv", index=False)