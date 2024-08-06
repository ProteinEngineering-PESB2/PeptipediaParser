import pandas as pd
import os
from Bio import SeqIO
from utils import raw_folder, parse_df, parsed_folder
try:
    dfs = []
    raw_folder = f"{raw_folder}/erop_moscow/"
    references = pd.read_csv(f"{raw_folder}/references.csv")
    for file in os.listdir(raw_folder):
        path = os.path.join(raw_folder, file)
        a = pd.DataFrame([[str(a.id).split("|")[0], str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["id", "sequence"])
        a["activity"] = file.replace(".fasta", "")
        dfs.append(a)
    df = pd.concat(dfs)
    references.pubmed = references.pubmed.map(eval)
    df = df.merge(references, on="id", how="left")
    df = df.explode("pubmed")
    df = df.dropna(subset=["sequence"])
    df["sequence"] = df["sequence"].str.replace("+", "")
    df["sequence"] = df["sequence"].str.replace("-", "")
    df = parse_df(df)
    df = df.drop(columns=["id"])
    df.to_csv(f"{parsed_folder}/erop_moscow.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)