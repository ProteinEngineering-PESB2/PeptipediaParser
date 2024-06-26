from os import listdir
from Bio import SeqIO
import pandas as pd
from functions import verify_sequences
import os

full_data = []
raw_folder = "../../raw_data/amplify/"
dfs = []
for filename in listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
    a["activity"] = "antimicrobial"
    dfs.append(a)
df = pd.concat(dfs)
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv(os.path.join("../../parsed_data/amplify.csv"), index=False)