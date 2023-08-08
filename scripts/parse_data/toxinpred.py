import pandas as pd
import os
from functions import verify_sequences
dfs = []
raw_folder = "../../raw_data/toxinpred/"
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    df = pd.read_csv(path, header=None)
    df.columns = ["sequence"]
    df["activity"] = "toxic"
    dfs.append(df)
df = pd.concat(dfs)
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/toxinpred.csv", index=False)