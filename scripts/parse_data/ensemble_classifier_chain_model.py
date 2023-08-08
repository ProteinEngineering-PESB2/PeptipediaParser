import os
import pandas as pd
from functions import verify_sequences
raw_folder = "../../raw_data/ensemble_classifier_chain_model/"
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
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/ensemble_classifier_chain_model.csv", index=False)