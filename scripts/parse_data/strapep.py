import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/strapep/data.csv")
df = df[["Sequence", "Classification"]].rename(columns={"Classification": "activity", "Sequence": "sequence"})

df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df.activity = df.activity.str.lower()
replace_dict = {"toxin and venom peptide": "toxic", "cytokine/growth factor": "cytokines / growth factor", "other": ""}
df.activity = df.activity.replace(replace_dict)
print(df)
df.to_csv("../../parsed_data/strapep.csv", index=False)