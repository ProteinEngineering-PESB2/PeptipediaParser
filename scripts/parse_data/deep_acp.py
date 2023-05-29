from Bio import SeqIO
import pandas as pd
from functions import verify_sequences
a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse("../../raw_data/deepacp/ACPs10.txt", "fasta"))], columns=["sequence"])
b = pd.DataFrame([[str(b.seq)] for b in list(SeqIO.parse("../../raw_data/deepacp/ACPs82.txt", "fasta"))], columns=["sequence"])
c = pd.DataFrame([[str(c.seq)] for c in list(SeqIO.parse("../../raw_data/deepacp/ACPs250.txt", "fasta"))], columns=["sequence"])
df = pd.concat([a, b, c])
df["activity"] = "anticancer"
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/deepacp.csv", index=False)