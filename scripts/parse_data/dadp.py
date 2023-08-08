import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/dadp/dadp.csv")
df = df[["Bioactive sequence"]].rename(columns={"Bioactive sequence": "sequence"})
df["activity"] = "anuran defense"
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df[df["sequence"] != "/"]
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/dadp.csv", index=False)