import os
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
try:
    raw_folder = f"{raw_folder}/pep-lab_db/"
    dfs = []
    for file in os.listdir(raw_folder):
        path = os.path.join(raw_folder, file)
        df = pd.read_csv(path, sep=";")
        dfs.append(df)
    df = pd.concat(dfs)
    df = df[["sequence", "activity"]]
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df2 = df.copy()
    df2.activity = "Nutraceutical"
    df = pd.concat([df, df2])
    df.to_csv(f"{parsed_folder}/pep-lab_db.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)