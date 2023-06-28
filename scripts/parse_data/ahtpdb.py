import pandas as pd
import os
from functions import verify_sequences

raw_folder = "../../raw_data/ahtpdb/"
dfs = []
for filename in os.listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    data = pd.read_csv(path, sep="\t")
    data = data[["seq "]]
    data["activity"] = "anti hypertensive"
    data = data.rename(columns={"seq ": "sequence"})
    dfs.append(data)

df = pd.concat(dfs)
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv(os.path.join("../../parsed_data/ahtpdb.csv"), index=False)
