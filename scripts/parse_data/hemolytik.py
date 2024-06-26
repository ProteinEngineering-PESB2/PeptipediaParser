import pandas as pd
import os
from Bio import SeqIO
from functions import verify_sequences
dfs = []
raw_folder = "../../raw_data/hemolytik/"
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    a = pd.read_csv(path).rename(columns={"SEQUENCE": "sequence"})[["sequence"]]
    a["activity"] = file.replace(".csv", "").lower()
    dfs.append(a)
df = pd.concat(dfs)
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
replace_dict = {"toxi": "toxic", "cpp": "cell penetrating", "antiparasitic": "anti parasitic"}
print(df.activity.unique())
df.activity = df.activity.replace(replace_dict)
print(df)
df.to_csv("../../parsed_data/hemolytik.csv", index=False)