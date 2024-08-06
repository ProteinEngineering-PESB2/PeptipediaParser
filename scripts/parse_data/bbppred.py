"""BBPPRED"""
from os import listdir
from Bio import SeqIO
import pandas as pd
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    full_data = []
    raw_folder = f"{raw_folder}/bbppred/BBPpred_datasets/"
    dfs = []
    for filename in listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        a = pd.DataFrame([[a.id.split("|")[1], str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["activity", "sequence"])
        a = a[a.activity == "1"]
        a["activity"] = "blood brain barrier penetrating"
        dfs.append(a)
    df = pd.concat(dfs)
    df = df[["sequence", "activity"]]
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/bbppred.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)
