#Signal Sequence
import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/signalpeptide/signalpeptide.csv")
df = df[["Signal Sequence"]].rename(columns={"Signal Sequence": "sequence"})
df["activity"] = "signal"
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/signalpeptide.csv", index=False)