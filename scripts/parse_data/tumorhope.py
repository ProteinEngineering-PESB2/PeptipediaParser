import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    df = pd.read_csv(f"{raw_folder}/tumorhope/tumorhope.csv")
    df = df[["Sequence", "Homing/targeting"]].rename(columns={"Sequence": "sequence", "Homing/targeting": "activity"})
    df["prefix"] = "tumor-"
    df["activity"] = df.prefix + df.activity
    df = df[["sequence", "activity"]]
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/tumorhope.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)