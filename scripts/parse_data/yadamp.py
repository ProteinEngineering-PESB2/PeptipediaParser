import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/yadamp/data.csv")
df = df[df["0"].str.contains("SEQ")][["0"]]
df = df.rename(columns={"0": "sequence"})
df["sequence"] = df["sequence"].replace("SEQ: ", "", regex=True)
df["activity"] = "antimicrobial"
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/yadamp.csv", index=False)