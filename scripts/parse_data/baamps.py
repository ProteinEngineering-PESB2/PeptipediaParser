import pandas as pd
df = pd.read_csv("../../raw_data/baamps/BAAMPs_data.csv", skiprows=1)
df = df[["PeptideSequence", "Microorganism group"]]
df["activity"] = '["antibiofilm", "antimicrobial"]'
df["activity"] = df["activity"].map(eval)
df = df.explode("activity")
df = df.rename(columns={"PeptideSequence": "sequence"})
df = pd.concat([
    df[["sequence", "Microorganism group"]].rename(columns={"Microorganism group": "activity"}),
    df[["sequence", "activity"]]
])
df = df.drop_duplicates()
df = df.dropna()
df = df.replace("gram neg", "gram-negative")
df = df.replace("gram pos", "gram-positive")
df = df.replace("yeast or fungus", "antifungal")
print(df)
df.to_csv("../../parsed_data/baamps.csv", index=False)