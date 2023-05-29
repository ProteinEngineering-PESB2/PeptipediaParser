import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/biodadpep/biodadpep.csv")
df = df[["Peptide Sequence", "Type 1 Diabetes/Type 2 Diabetes"]]
df["activity"] = "antidiabetic"
df = df.rename(columns={"Peptide Sequence": "sequence", "Type 1 Diabetes/Type 2 Diabetes": "type"})
df = pd.concat([
    df[["sequence", "type"]].rename(columns={"type": "activity"}),
    df[["sequence", "activity"]]
])
df = df.replace({"Type 1 Diabetes": "type 1 diabetes", "Type 2 Diabetes": "type 2 diabetes"})
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/biodadpep.csv", index=False)