"""AntiCP"""
import os
import pandas as pd
from utils import  parse_df, parsed_folder, raw_folder
try:
    raw_folder = f"{raw_folder}/anticp/"
    dfs = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        data = pd.read_csv(path, header=None)
        data["activity"] = "anticancer"
        data = data.rename(columns={0: "sequence"})
        dfs.append(data)
    df = pd.concat(dfs)
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/anticp.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)