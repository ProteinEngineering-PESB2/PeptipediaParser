import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/baamps/BAAMPs_data.csv", skiprows=1)
df = df[["PeptideSequence", "Microorganism group"]]
df["activity"] = '["anti biofilm", "antimicrobial"]'
df["activity"] = df["activity"].map(eval)
df = df.explode("activity")
df = df.rename(columns={"PeptideSequence": "sequence"})
df = pd.concat([
    df[["sequence", "Microorganism group"]].rename(columns={"Microorganism group": "activity"}),
    df[["sequence", "activity"]]
])
df = df.drop_duplicates()
df = df.dropna()
df = df.replace("gram neg", "anti gram negative")
df = df.replace("gram pos", "anti gram positive")
df = df.replace("yeast or fungus", "antifungal")
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/baamps.csv", index=False)