import pandas as pd
df = pd.read_csv("../../raw_data/yadamp/data.csv")
df = df[df["0"].str.contains("SEQ")][["0"]]
df = df.rename(columns={"0": "sequence"})
df["sequence"] = df["sequence"].replace("SEQ: ", "", regex=True)
print(df)
df.to_csv("../../parsed_data/yadamp.csv", index=False)