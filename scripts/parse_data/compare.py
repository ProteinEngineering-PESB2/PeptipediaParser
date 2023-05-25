import pandas as pd
from Bio import SeqIO

sequences = [str(record.seq) for record in SeqIO.parse("../../raw_data/compare/COMPARE-2023-FastA-Seq.txt", "fasta")]
df = pd.DataFrame()
df["sequence"] = sequences
df["activity"] = "allergen"
df = df.drop_duplicates()
df = df[df.sequence.str.len() <= 150]
df.to_csv("../../parsed_data/compare.csv", index=False)