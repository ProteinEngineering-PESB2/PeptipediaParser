"""APD3"""
import os
import pandas as pd
from utils import parse_df, raw_folder, parsed_folder

try:
    full_data = []
    raw_folder = f"{raw_folder}/apd3/"
    dfs = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        a = pd.read_csv(path)
        a["activity"] = ".".join(filename.split(".")[:-1])
        dfs.append(a)
    df = pd.concat(dfs)
    df = df.rename(columns={"1": "sequence"})
    df = df[["sequence", "activity"]]
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/apd3.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)