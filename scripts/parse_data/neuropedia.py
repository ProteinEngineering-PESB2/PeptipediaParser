import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    df = pd.read_excel(f"{raw_folder}/neuropedia/Database_NeuroPedia_063011.xls", skiprows=1)
    df["sequence"] = df[["Amino acid Sequence"]]
    df = df[["sequence"]]
    df[["activity"]] = "neuropeptide"
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/neuropedia.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)