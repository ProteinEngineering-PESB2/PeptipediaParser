from Bio import SeqIO
import pandas as pd
from functions import verify_sequences
records = SeqIO.parse("../../raw_data/cppsite/natural_pep.fa", "fasta")
sequences = [str(a.seq) for a in records]
df = pd.DataFrame()
df["sequence"] = sequences
df["activity"] = "cell penetrating"
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/cppsite.csv", index=False)