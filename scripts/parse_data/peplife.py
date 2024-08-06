"""Aaging"""
import os
import pandas as pd
from utils import parse_df, raw_folder, parsed_folder
try:
    df = pd.read_csv(f"{raw_folder}/peplife/peplife.tsv", sep="\t")
    df = df[["SEQUENCE", "HALF LIFE", "UNITS OF HALF LIFE"]]
    df = df.rename(columns={"SEQUENCE": "sequence", "HALF LIFE": "half_life"})
    df["half_life"] = df["half_life"] + " " + df["UNITS OF HALF LIFE"]
    df = df.drop(columns=["UNITS OF HALF LIFE"])
    df = df.groupby(by=["sequence"], as_index = False)["half_life"].apply(lambda x: ', '.join(x))
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/peplife.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)