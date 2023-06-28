import os
import pandas as pd
parsed_folder = "../parsed_data/"
dfs = []
for file in os.listdir(parsed_folder):
    path = os.path.join(parsed_folder, file)
    db = pd.read_csv(path)
    db["source"] = file.split(".")[0]
    dfs.append(db)
df = pd.concat(dfs)
df = df.replace("-", " ", regex=True)
df = df.replace(r"\s+", " ", regex=True)
df.to_csv("../data.csv", index=False)

a = df[["sequence", "source"]].drop_duplicates()
sources = a.value_counts(subset=["source"])
sources = sources.sort_values(ascending=False)
sources.to_csv("../sources.csv", index=True)

a = df[["sequence", "activity"]].drop_duplicates()
activities = a.value_counts(subset=["activity"])
activities = activities.sort_values(ascending=False)
activities.to_csv("../activities.csv", index=True)

a = df[df.activity.notna()]

sequences = a.sequence.drop_duplicates()
sequences.to_csv("../all_peptides.csv", index=False)

a = df[["sequence", "activity"]].drop_duplicates()
a["value"] = 1
a = a.dropna()
a = a.pivot(index="sequence", columns="activity", values="value")
a = a.fillna(0)
a.to_csv("../activity_pivot.csv", index=True)
