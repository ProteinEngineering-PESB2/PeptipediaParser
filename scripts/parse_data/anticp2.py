import pandas as pd
import os
from utils import raw_folder, parsed_folder, parse_df
try:
    raw_folder = f"{raw_folder}/anticp2/"
    dfs = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        data = pd.read_csv(path, header=None)
        data["activity"] = "anticancer"
        data = data.rename(columns={0: "sequence"})
        dfs.append(data)
    df = pd.concat(dfs)
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/anticp2.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)