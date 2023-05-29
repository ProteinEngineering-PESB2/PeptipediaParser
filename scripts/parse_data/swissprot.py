import pandas as pd
from Bio import SeqIO
from functions import verify_sequences

pdb_path = "../../raw_data/swissprot/uniprot_sprot.fasta"
df = pd.DataFrame([[a.description, str(a.seq)] for a in list(SeqIO.parse(pdb_path, "fasta"))], columns=["id", "sequence"])
df = df[["sequence"]]
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/swissprot.csv", index=False)