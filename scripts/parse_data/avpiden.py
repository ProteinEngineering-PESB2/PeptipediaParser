"""AVPIC50Pred"""
from os import listdir
import pandas as pd
from Bio import SeqIO
from utils import parse_df, parsed_folder, raw_folder
import os
try:
    full_data = []
    raw_folder = f"{raw_folder}/avpiden/"
    dfs = []
    for filename in listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        a =  pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
        a["activity"] = filename.split(".")[0]
        dfs.append(a)
    df = pd.concat(dfs)
    df = df[["sequence", "activity"]]
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/avpiden.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)