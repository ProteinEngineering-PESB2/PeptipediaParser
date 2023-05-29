from Bio import SeqIO
import pandas as pd
from functions import verify_sequences
records = SeqIO.parse("../../raw_data/conoserver/conoserver_protein.fa", "fasta")
df = [[str(record.description), str(record.seq)] for record in records]
df = pd.DataFrame(df, columns=["description", "sequence"])
df["activity"] = df.description.str.contains("toxin")
df = df.replace(True, "toxic")
df = df.replace(False, None)
df = df[["sequence", "activity"]]
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/conoserver.csv", index=False)