import pandas as pd
from Bio import SeqIO
from functions import verify_sequences

pdb_path = "../../raw_data/rcsb_pdb/pdb_seqres.txt"
df = pd.DataFrame([[a.description, str(a.seq)] for a in list(SeqIO.parse(pdb_path, "fasta"))], columns=["id", "sequence"])
df = df[df.id.str.contains("protein")]
df = df[["sequence"]]
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/rcsb_pdb.csv", index=False)