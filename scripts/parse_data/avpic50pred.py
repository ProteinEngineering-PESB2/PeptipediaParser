from os import listdir
import pandas as pd
from functions import verify_sequences
import os

full_data = []
raw_folder = "../../raw_data/avpic50pred/"
dfs = []
for filename in listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    a = pd.read_csv(path)
    dfs.append(a)
df = pd.concat(dfs)
df = df.rename(columns={"Sequence": "sequence"})
df = df[["sequence"]]
df["activity"] = "antiviral"
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv(os.path.join("../../parsed_data/avpic50pred.csv"), index=False)