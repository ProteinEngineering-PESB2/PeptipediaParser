import pandas as pd
from functions import verify_sequences
df = pd.read_excel("../../raw_data/neuropedia/Database_NeuroPedia_063011.xls", skiprows=1)
df["sequence"] = df[["Amino acid Sequence"]]
df = df[["sequence"]]
df[["activity"]] = "neuropeptide"
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/neuropedia.csv", index=False)