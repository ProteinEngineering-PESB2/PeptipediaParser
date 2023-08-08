from Bio import SeqIO
import pandas as pd
import os
from os import makedirs
from functions import verify_sequences
raw_folder = "../../raw_data/acp_dl/"
parsed_folder = "../../parsed_data/"
makedirs(parsed_folder, exist_ok=True)

full_data = []
for filename in os.listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    data = [[str(a.seq), a.description.split("|")[1]]
            for a in list(
                SeqIO.parse(path, "fasta"))]
    df = pd.DataFrame(data, columns=["sequence", "activity"])
    full_data.append(df)
df = pd.concat(full_data)
df = df[df.activity == "1"]
df["activity"] = "anticancer"
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv(os.path.join("../../parsed_data/acp_dl.csv"), index=False)