import pandas as pd
import os
from functions import verify_sequences

raw_folder = "../../raw_data/antitbpdb/"
dfs = []
for filename in os.listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    data = pd.read_csv(path)
    data["activity"] = "anti tubercular"
    data = data.rename(columns={"Sequence": "sequence"})
    dfs.append(data)
df = pd.concat(dfs)
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df = df[["sequence", "activity", "is_canon"]]
print(df)
df.to_csv(os.path.join("../../parsed_data/antitbpdb.csv"), index=False)
