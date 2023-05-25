from Bio import SeqIO
import pandas as pd
a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse("../../raw_data/deep_acp/ACPs10.txt", "fasta"))], columns=["sequence"])
b = pd.DataFrame([[str(b.seq)] for b in list(SeqIO.parse("../../raw_data/deep_acp/ACPs82.txt", "fasta"))], columns=["sequence"])
c = pd.DataFrame([[str(c.seq)] for c in list(SeqIO.parse("../../raw_data/deep_acp/ACPs250.txt", "fasta"))], columns=["sequence"])
df = pd.concat([a, b, c])
df["activity"] = "anticancer"
df.to_csv("../../parsed_data/deep_acp.csv", index=False)