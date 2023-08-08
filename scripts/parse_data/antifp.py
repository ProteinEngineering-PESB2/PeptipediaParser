import pandas as pd
import os
from functions import verify_sequences

raw_folder = "../../raw_data/antifp/"
dfs = []
for filename in os.listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    data = pd.read_csv(path, header=None)
    data["activity"] = "antifungal"
    data = data.rename(columns={0: "sequence"})
    dfs.append(data)
df = pd.concat(dfs)
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv(os.path.join("../../parsed_data/antifp.csv"), index=False)
