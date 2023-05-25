import pandas as pd
from Bio import SeqIO
train = [str(a.seq) for a in SeqIO.parse("../raw_data/preaip/train.fasta", format="fasta") if "Positive" in a.id]
test = [str(a.seq) for a in SeqIO.parse("../raw_data/preaip/test.fasta", format="fasta")]

sequences = train + test

df = pd.DataFrame()
df["sequence"] = sequences
df["activity"] = "antiinflamatory"
df.to_csv("../parsed_data/preaip.csv", index=False)
print(df)