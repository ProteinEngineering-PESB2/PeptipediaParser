import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/brainpeps/brainpeps.csv")
df = df.rename(columns={"Sequence": "sequence"})
df["activity"] = "blood-brain barrier penetrating"
df = df[["sequence", "activity"]]
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/brainpeps.csv", index=False)