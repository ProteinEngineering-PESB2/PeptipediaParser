import pandas as pd
import os
from Bio import SeqIO
from functions import verify_sequences
dfs = []
raw_folder = "../../raw_data/plantpepdb/"
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    df = pd.read_csv(path, sep="\t")
    #df.columns = ["sequence"]
    #df["activity"] = file.replace(".txt", "")
    dfs.append(df)
df = pd.concat(dfs)
print(df)
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/peptidedb.csv", index=False)