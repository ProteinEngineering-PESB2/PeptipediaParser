import pandas as pd
import os
from utils import parse_df, raw_folder, parsed_folder
try:
    raw_folder = f"{raw_folder}/ahtpdb/"
    dfs = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        data = pd.read_csv(path, sep="\t")
        data = data[["seq "]]
        data["activity"] = "anti hypertensive"
        data = data.rename(columns={"seq ": "sequence"})
        dfs.append(data)
    df = pd.concat(dfs)
    df = df.replace("ND", None)
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/ahtpdb.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)