import pandas as pd
from Bio import SeqIO
train = [str(a.seq) for a in SeqIO.parse("../raw_data/predneurop/pos_train.fasta", format="fasta")]
test = [str(a.seq) for a in SeqIO.parse("../raw_data/predneurop/pos_test.fasta", format="fasta")]

sequences = train + test

df = pd.DataFrame()
df["sequence"] = sequences
df["activity"] = "neuropeptide"
df.to_csv("../parsed_data/predneurop.csv", index=False)
print(df)