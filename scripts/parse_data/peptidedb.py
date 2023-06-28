import pandas as pd
import os
from Bio import SeqIO
from functions import verify_sequences
dfs = []
replace = {"Peptide Hormones": "hormone",
           "Antimicrobial peptides": "antimicrobial" ,
           "Cytokines and growth factor": "cytokines / growth factor",
           "Toxins and venom peptides": "toxic",
           "Antifreeze": "anti freeze", "Other families": "",
           "Unique peptides": ""
           }
raw_folder = "../../raw_data/peptidedb/"
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    df = pd.read_csv(path, header=None)
    df.columns = ["sequence"]
    df["activity"] = file.replace(".txt", "")
    dfs.append(df)
df = pd.concat(dfs)
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df.activity = df.activity.map(replace)
print(df)
df.to_csv("../../parsed_data/peptidedb.csv", index=False)