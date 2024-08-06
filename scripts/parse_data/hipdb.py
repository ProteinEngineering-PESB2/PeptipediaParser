import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
def separate_pubmed_patent(text):
    try:
        int(text)
        return [text, None]
    except:
        if "US" in text:
            return [None, text]
        return [text, None]
try:
    df = pd.read_excel(f"{raw_folder}/hipdb/HIPdb_data.xls")
    df = df[["SEQUENCE", "PMID"]]
    df["activity"] = "antiviral"
    df = df.rename(columns={"SEQUENCE": "sequence", "PMID": "pubmed"})
    df = df.dropna(subset=["sequence"])
    df["pubmed"], df["patent"] = zip(*df.pubmed.map(separate_pubmed_patent))
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/hipdb.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)