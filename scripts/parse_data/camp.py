import os
import pandas as pd
data = []
for a in os.listdir("../../raw_data/camp/"):
    a = pd.read_csv(f"../../raw_data/camp/{a}", sep="\t")
    data.append(a)
df = pd.concat(data)
df = df[["Activity", "Gram_Nature", "Seqence"]]
df = df.drop_duplicates()
df["Activity"] = df["Activity"].str.replace(" ", "").str.split(",")
df["Gram_Nature"] = df["Gram_Nature"].str.replace(" ", "").str.split(",")
df = pd.concat([
    df[["Seqence", "Activity"]],
    df[["Seqence", "Gram_Nature"]].rename(columns = {"Gram_Nature": "Activity"})
])
df = df.explode("Activity")
df = df.replace("Gram+ve", "gram-positive")
df = df.replace("Gram-ve", "gram-negative")
df = df.rename(columns={"Seqence": "sequence", "Activity": "activity"})
df.activity = df.activity.str.lower()
df = df.drop_duplicates()
df = df[df.sequence.str.len() <= 150]
df.to_csv("../../parsed_data/camp.csv", index=False)
print(df)