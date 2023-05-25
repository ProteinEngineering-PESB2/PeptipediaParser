import os
import pandas as pd
from Bio import SeqIO
a = pd.DataFrame()
sequences_total = []
for file in os.listdir("../../raw_data/peptideatlas/"):
    records = SeqIO.parse(f"../../raw_data/peptideatlas/{file}", "fasta")
    sequences = [str(a.seq) for a in records]
    sequences_total += sequences
a["sequences"] = sequences_total
a.to_csv("../../parsed_data/peptideatlas.csv", index=False)