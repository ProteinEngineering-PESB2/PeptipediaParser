"""Brainpeps"""
import os
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
try:
    df = pd.read_csv(f"{raw_folder}/brainpeps/brainpeps.csv")
    df = df.rename(columns={"Sequence": "sequence"})
    df["activity"] = "blood brain barrier penetrating"
    df = df[["sequence", "activity"]]
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/brainpeps.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)
