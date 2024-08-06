"""Aaging"""
import os
import pandas as pd
from utils import parse_df, raw_folder, parsed_folder
try:
    df = pd.read_csv(f"{raw_folder}/plifepred/plifepred.txt", sep="\t")
    df = df[["Sequence", "Half-life(Seconds)"]]
    df = df.rename(columns={"Sequence": "sequence", "Half-life(Seconds)": "half_life"})
    df["half_life"] = df["half_life"].astype(str) + " seconds"
    df = df.groupby(by=["sequence"], as_index = False)["half_life"].apply(lambda x: ', '.join(x))
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/plifepred.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)