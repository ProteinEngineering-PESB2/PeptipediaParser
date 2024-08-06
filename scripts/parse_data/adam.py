"""ADAM"""
import os
import pandas as pd
from utils import parse_df, raw_folder, parsed_folder
try:
    raw_folder = f"{raw_folder}/adam/"
    path = os.path.join(raw_folder, "data.csv")
    df = pd.read_csv(path, header=None)[[2]]
    df = df.rename(columns={2: "sequence"})
    df["activity"] = "antimicrobial"
    df = parse_df(df)
    df.to_csv(parsed_folder + "adam.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)
