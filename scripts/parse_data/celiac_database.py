import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/celiac_database/Celiac Database.csv")
df = df[["Sequence", "Toxicity"]]
df = df.rename(columns={"Sequence": "sequence", "Toxicity": "activity"})

df["activity"] = df["activity"] + "-celiac"
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)

df.to_csv("../../parsed_data/celiac_database.csv", index=False)