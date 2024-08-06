"""AcovPepDB"""
import os
import pandas as pd
from utils import parse_df, raw_folder, parsed_folder
try:
    df = pd.read_csv(f"{raw_folder}/acovpepdb/ACovPepDB_Data_Entirety.csv")
    df = df[["Sequence", "Reference"]]
    df = df.rename(columns={"Sequence": "sequence", "Reference": "pubmed"})
    df["activity"] = "Anti Sars-Cov 2"
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/acovpepdb.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)