"""AVPIC50Pred"""
from os import listdir
import pandas as pd
from utils import separate_pubmed_patent, parse_df, parsed_folder, raw_folder
import os
try:
    full_data = []
    raw_folder = f"{raw_folder}/avpic50pred/"
    dfs = []
    for filename in listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        a = pd.read_csv(path)
        dfs.append(a)
    df = pd.concat(dfs)
    df = df.rename(columns={"Sequence": "sequence"})
    df["pubmed"], df["patent"] = zip(*df["Reference"].map(separate_pubmed_patent))
    df["activity"] = "antiviral"
    df = df[["sequence", "activity", "pubmed", "patent"]]
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/avpic50pred.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)