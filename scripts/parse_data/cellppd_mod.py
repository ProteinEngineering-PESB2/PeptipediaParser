import pandas as pd
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    raw_folder = f"{raw_folder}/cellppd_mod/"
    dfs = []
    for filename in os.listdir(raw_folder):
        df = pd.read_csv(raw_folder + filename, header=None)
        dfs.append(df)
    df = pd.concat(dfs)
    df = df.rename(columns={0: "sequence"})
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df["activity"] = "cell penetrating"
    df.to_csv(f"{parsed_folder}/cellppd_mod.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)