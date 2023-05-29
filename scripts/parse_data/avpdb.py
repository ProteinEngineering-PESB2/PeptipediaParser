from Bio import SeqIO
import pandas as pd
import os
from functions import verify_sequences

raw_folder = "../../raw_data/avpdb/"
filename = "AVPdb_data.tsv"
path = os.path.join(raw_folder, filename)
df = pd.read_csv(path, sep="\t")
df = df.rename(columns={"Sequence": "sequence"})
df = df[["sequence"]]
df["activity"] = "antiviral"
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv(os.path.join("../../parsed_data/avpdb.csv"), index=False)
