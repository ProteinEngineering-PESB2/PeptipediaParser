import pandas as pd
import os
from functions import verify_sequences
raw_folder = "../../raw_data/cellppd_mod/"
dfs = []
for filename in os.listdir(raw_folder):
    df = pd.read_csv(raw_folder + filename, header=None)
    dfs.append(df)
df = pd.concat(dfs)
df = df.rename(columns={0: "sequence"})
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df["activity"] = "cell penetrating"
print(df)
df.to_csv("../../parsed_data/cellppd_mod.csv", index=False)