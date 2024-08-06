"""Aaging"""
import os
import pandas as pd
from utils import parse_df, raw_folder, parsed_folder
try:
    df = pd.read_csv(f"{raw_folder}/aagingbase/aagingBase.csv")
    df = df[["Sequence"]]
    df = df.rename(columns={"Sequence": "sequence"})
    df["activity"] = "Anti aging"
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/aagingbase.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)