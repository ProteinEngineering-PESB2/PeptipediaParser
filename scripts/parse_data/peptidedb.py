import pandas as pd
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    dfs = []
    raw_folder = f"{raw_folder}/peptidedb/"
    for file in os.listdir(raw_folder):
        path = os.path.join(raw_folder, file)
        df = pd.read_csv(path, header=None)
        df.columns = ["sequence"]
        df["activity"] = file.replace(".txt", "")
        dfs.append(df)
    df = pd.concat(dfs)
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/peptidedb.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)