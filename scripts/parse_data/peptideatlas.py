import os
import pandas as pd
from Bio import SeqIO
from functions import verify_sequences
df = pd.DataFrame()
sequences_total = []
for file in os.listdir("../../raw_data/peptideatlas/"):
    records = SeqIO.parse(f"../../raw_data/peptideatlas/{file}", "fasta")
    sequences = [str(a.seq) for a in records]
    sequences_total += sequences
df["sequence"] = sequences_total
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/peptideatlas.csv", index=False)