"""AVPDB"""
import pandas as pd
import os
from utils import parse_df, parsed_folder, raw_folder
def separate_pubmed_patent(text):
    if "US" in text:
        return [None, text]
    return [text, None]
try:
    raw_folder = f"{raw_folder}/avpdb/"
    filename = "AVPdb_data.tsv"
    path = os.path.join(raw_folder, filename)
    df = pd.read_csv(path, sep="\t")
    df["activity"] = "Anti " + df[["Virus"]]
    df = df.rename(columns={"Sequence": "sequence"})
    df["pubmed"] = df["Accession"]
    df = parse_df(df)
    df = df[["sequence", "is_canon", "activity", "pubmed"]]
    df["pubmed"], df["patent"] = zip(*df.pubmed.map(separate_pubmed_patent))
    df.to_csv(os.path.join(f"{parsed_folder}/avpdb.csv"), index=False)

    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)