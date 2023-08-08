import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/cancer_ppd/mix_natural.txt", sep="\t", engine="python")
df["activity"] = "anticancer"
df = df.dropna()
df = df.rename(columns={"Sequence": "sequence"})
df = df[["sequence", "activity"]]
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/cancer_ppd.csv", index=False)