from Bio import SeqIO
import pandas as pd
from functions import verify_sequences
df = pd.read_csv("../../raw_data/bactibase/bactibase.csv")
swissprot = "../../raw_data/swissprot/uniprot_sprot.fasta"
swissprot = pd.DataFrame([[a.id.split("|")[1], str(a.seq)] for a in list(SeqIO.parse(swissprot, "fasta"))], columns=["id", "sequence"])
df = df.merge(swissprot, left_on="UniProt", right_on="id")
df = df[["sequence"]]
df["activity"] = '["bacteriocin", "antimicrobial", "antibacterial"]'
df["activity"] = df["activity"].map(eval)
df = df.explode("activity")
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/bactibase.csv", index=False)