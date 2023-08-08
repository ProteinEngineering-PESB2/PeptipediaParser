from Bio import SeqIO
import pandas as pd
from functions import verify_sequences
parsed_folder = "../../parsed_data/"
records = SeqIO.parse("../../raw_data/compare/COMPARE-2023-FastA-Seq.txt", "fasta")
data = [[str(a.seq)] for a in records]
df = pd.DataFrame(data, columns=["sequence"])
df["activity"] = "allergen"
df = df.dropna(subset=["sequence"])
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv(f"{parsed_folder}/compare.csv", index=False)