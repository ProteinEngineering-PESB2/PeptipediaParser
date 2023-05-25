from Bio import SeqIO
import pandas as pd
records = SeqIO.parse("../../raw_data/cppsite/cppsite.fasta", "fasta")
sequences = [str(a.seq) for a in records]
data = pd.DataFrame()
data["sequence"] = sequences
data["activity"] = "cell-penetrating"
print(data)
data.to_csv("../../parsed_data/cppsite.csv", index=False)