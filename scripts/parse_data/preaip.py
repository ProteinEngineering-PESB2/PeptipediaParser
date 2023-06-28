import pandas as pd
from Bio import SeqIO
from functions import verify_sequences
train = [str(a.seq) for a in SeqIO.parse("../../raw_data/preaip/test-positive.txt", format="fasta")]
test = [str(a.seq) for a in SeqIO.parse("../../raw_data/preaip/training-positive.txt", format="fasta")]

sequences = train + test

df = pd.DataFrame()
df["sequence"] = sequences
df["activity"] = "anti inflammatory"
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/preaip.csv", index=False)
