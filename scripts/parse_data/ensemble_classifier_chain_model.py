import os
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
try:
    raw_folder = f"{raw_folder}/ensemble_classifier_chain_model/"
    dfs = []
    for file in os.listdir(raw_folder):
        path = os.path.join(raw_folder, file)
        df = pd.read_csv(path, sep="##", header=None)
        df.columns=["id", "sequence"]
        dfs.append(df)
    df = pd.concat(dfs)
    df["activity"] = "anti inflammatory"
    df = df[["sequence", "activity"]]
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/ensemble_classifier_chain_model.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)