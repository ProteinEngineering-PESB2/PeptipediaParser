import pandas as pd
from functions import verify_sequences
data = []
df = pd.read_csv("../../raw_data/camp/CAMP_2023-05-26 20-14-20.txt", sep="\t")
df = df[["Activity", "Gram_Nature", "Seqence"]]
df = df.drop_duplicates()
df["Activity"] = df["Activity"].str.replace(" ", "").str.split(",")
df["Gram_Nature"] = df["Gram_Nature"].str.replace(" ", "").str.split(",")
df = pd.concat([
    df[["Seqence", "Activity"]],
    df[["Seqence", "Gram_Nature"]].rename(columns = {"Gram_Nature": "Activity"})
])
df = df.explode("Activity")
replace_dict = {"gram+ve": "anti gram positive",
                "gram-ve": "anti gram negative",
                "gram-": "anti gram negative", "gram+": "anti gram positive",
                "antiparasitic": "anti parasitic",
                None: "", "ram+ve": "anti gram positive", "antitumour": "antitumor"
                }
df = df.rename(columns={"Seqence": "sequence", "Activity": "activity"})
df.activity = df.activity.str.split(".")
df = df.explode("activity")
df.activity = df.activity.str.lower()
df.activity = df.activity.replace(replace_dict)
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/camp.csv", index=False)