"""AntiTBPDB"""
import os
import pandas as pd
from utils import parse_df, raw_folder, parsed_folder, separate_pubmed_patent

try:
    raw_folder = f"{raw_folder}/antitbpdb/"
    dfs = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        data = pd.read_csv(path)
        data["activity"] = "anti tubercular"
        data = data.rename(columns={"Sequence": "sequence"})
        dfs.append(data)
    df = pd.concat(dfs)
    df = parse_df(df)
    df["pubmed"], df["patent"] = zip(*df["Pubmed ID/ Patent No."]
                                  .map(separate_pubmed_patent))
    df = df[["sequence", "activity", "is_canon", "patent", "pubmed"]]
    df.to_csv(os.path.join(f"{parsed_folder}/antitbpdb.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)