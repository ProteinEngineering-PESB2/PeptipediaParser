import pandas as pd
from Bio import SeqIO
a = [[str(a.seq), a.description.split("|")[-1]] for a in list(SeqIO.parse("../raw_data/iACP-DRLF/ACP20AltTest.fasta", "fasta"))]
b = [[str(a.seq), a.description.split("|")[-1]] for a in list(SeqIO.parse("../raw_data/iACP-DRLF/ACP20AltTrain.fasta", "fasta"))]
c = [[str(a.seq), a.description.split("|")[-1]] for a in list(SeqIO.parse("../raw_data/iACP-DRLF/ACP20mainTest.fasta", "fasta"))]
d = [[str(a.seq), a.description.split("|")[-1]] for a in list(SeqIO.parse("../raw_data/iACP-DRLF/ACP20mainTrain.fasta", "fasta"))]
a = pd.DataFrame(a, columns=["sequence", "activity"])
b = pd.DataFrame(b, columns=["sequence", "activity"])
c = pd.DataFrame(c, columns=["sequence", "activity"])
d = pd.DataFrame(d, columns=["sequence", "activity"])
df = pd.concat([a, b, c, d])
df = df[df.activity == "1"]
df = df.replace("1", "anticancer")
print(df)
df.to_csv("../parsed_data/iACP-DRLF.csv", index=False)