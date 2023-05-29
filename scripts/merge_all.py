import os
import pandas as pd
parsed_folder = "./parsed_data/"
dfs = []
for file in os.listdir(parsed_folder):
    path = os.path.join(parsed_folder, file)
    db = pd.read_csv(path)
    db["source"] = file.split(".")[0]
    dfs.append(db)
df = pd.concat(dfs)

activities = df.value_counts(subset=["activity"])

print(activities)

print("Unique peptides:",len(df.sequence.unique()))
df = df[df.activity.notna()]
print("With activity peptides:",len(df.sequence.unique()))
