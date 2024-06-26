import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/tumorhope/tumorhope.csv")
df = df[["Sequence", "Homing/targeting"]].rename(columns={"Sequence": "sequence", "Homing/targeting": "activity"})
df["prefix"] = "tumor-"
df["activity"] = df.prefix + df.activity.str.lower()
df = df[["sequence", "activity"]]
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
replace_dict = {"tumor-homing (phage display clone)": "tumor-homing", "tumor-targeting & further studied": "tumor-targeting"}
df.activity = df.activity.replace(replace_dict)
print(df)
df.to_csv("../../parsed_data/tumorhope.csv", index=False)