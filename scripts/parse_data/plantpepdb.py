import pandas as pd
import os
import numpy as np
from utils import raw_folder, parse_df, parsed_folder
def separate_doi_pmid(text):
    try:
        float(text)
        return [None, text]
    except:
        if "doi.org" in text:
            return [text, None]
        if "www." in text:
            return [None, None]
        if "10." in text:
            return [text, None]
        return [None, text]

dfs = []
raw_folder = f"{raw_folder}/plantpepdb/"
path = raw_folder + "plantpepdb.csv"
df = pd.read_csv(path)
df = df[["sequence", "Peptide Activity", "PMID/DOI"]]
df = df.rename(columns={"Peptide Activity": "activity"})
df["PMID/DOI"] = df["PMID/DOI"].str.split(",")
df = df.explode("PMID/DOI")
df["PMID/DOI"] = df["PMID/DOI"].str.strip()
df["PMID/DOI"] = df["PMID/DOI"].replace("--NA--", np.nan)
df["doi"], df["pubmed"] = zip(*df["PMID/DOI"].map(separate_doi_pmid))
df = df.drop(columns=["PMID/DOI"])
df["activity"] = df.activity.str.split(", ")
df = df.explode("activity")
df = parse_df(df)
df.to_csv(f"{parsed_folder}/plantpepdb.csv", index=False)
print(os.path.basename(__file__), "success")