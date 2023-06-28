import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/biopep/biopep.csv")
df = df[["Sequence", "Activity"]]
df = df.rename(columns={"Sequence": "sequence", "Activity": "activity"})
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df["activity"] = df["activity"].str.lower()
replace_dict = {"antioxidant": "antioxidative", "anorectic": "anorexic", "haemolytic": "hemolytic", "immunomodulating": "immunomodulatory"}
df.activity = df.activity.replace(replace_dict)
print(df)
df.to_csv("../../parsed_data/biopep.csv", index=False)