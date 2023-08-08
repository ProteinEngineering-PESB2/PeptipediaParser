import pandas as pd
import os
from os import makedirs
from functions import verify_sequences

raw_folder = "../../raw_data/adam/"
parsed_folder = "../../parsed_data/"
makedirs(parsed_folder, exist_ok=True)
path = os.path.join(raw_folder, "data.csv")
df = pd.read_csv(path, header=None)[[2]]
df = df.rename(columns={2: "sequence"})
df["activity"] = "antimicrobial"
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)

df.to_csv(parsed_folder + "adam.csv", index=False)