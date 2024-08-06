import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    df = pd.read_csv(f"{raw_folder}/quorumpeps/quorumpeps.csv")
    df = df[["Sequence", "Reference"]].rename(columns={"Sequence": "sequence", "Reference": "pubmed"})
    df["activity"] = "quorum sensing"

    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/quorumpeps.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)