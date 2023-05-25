import pandas as pd
import os
raw_data = "../../raw_data/avpdb/"
dfs = []
for file in os.listdir(raw_data):
    path = os.path.join(raw_data, file)
    df = pd.read_csv(path, sep="\t")
    df = df[["Sequence"]].rename(columns={"Sequence": "sequence"})
    dfs.append(df)
df = pd.concat(dfs)
df["activity"] = "antiviral"
df.to_csv("../../parsed_data/avpdb.csv", index=False)