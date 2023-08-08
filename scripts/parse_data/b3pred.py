from Bio import SeqIO
import pandas as pd
import os
from functions import verify_sequences

raw_folder = "../../raw_data/b3pred/"
filename = "Positive_B3PPs.fasta"
path = os.path.join(raw_folder, filename)
df = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
df["activity"] = "blood brain barrier penetrating"
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv(os.path.join("../../parsed_data/b3pred.csv"), index=False)
