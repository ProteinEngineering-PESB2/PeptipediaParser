import pandas as pd
df = pd.read_csv("../../raw_data/biodadpep/biodadpep.csv")
df = df[["Peptide Sequence", "Type 1 Diabetes/Type 2 Diabetes"]]
df["activity"] = "antidiabetic"
df = df.rename(columns={"Peptide Sequence": "sequence", "Type 1 Diabetes/Type 2 Diabetes": "type"})
data = pd.concat([
    df[["sequence", "type"]].rename(columns={"type": "activity"}),
    df[["sequence", "activity"]]
])
data = data.drop_duplicates()
data = data[data.sequence.str.len() <= 150]
data.to_csv("../../parsed_data/biodadpep.csv", index=False)
print(data)