"""BIODADPEP"""
import os
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder

def separate_ref(text):
    if "PMID:" in text:
        return [None, text.split(":")[1]]
    if "10." in text:
        return [text.replace("doi: ", ""), None]
    return [None, None]
try:
    df = pd.read_csv(f"{raw_folder}/biodadpep/biodadpep.csv")
    df = df[["Peptide Sequence", "Type 1 Diabetes/Type 2 Diabetes", "References"]]

    df["References"] = df["References"].str.split(",")
    df = df.explode("References")
    df["References"] = df["References"].str.strip()


    df["References"] = df["References"].str.split(";")
    df = df.explode("References")
    df["References"] = df["References"].str.strip()

    df["doi"], df["pubmed"] = zip(*df.References.map(separate_ref))
    df = df.drop(columns=["References"])
    df["activity"] = "antidiabetic"
    df = df.rename(columns={"Peptide Sequence": "sequence", "Type 1 Diabetes/Type 2 Diabetes": "type"})
    df = pd.concat([
        df[["sequence", "type", "doi", "pubmed"]].rename(columns={"type": "activity"}),
        df[["sequence", "activity", "doi", "pubmed"]]
    ])
    df = df.drop_duplicates(subset=["sequence", "activity"])
    df.activity = df.activity.fillna("")
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/biodadpep.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)
