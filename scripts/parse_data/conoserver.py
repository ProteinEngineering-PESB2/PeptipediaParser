from Bio import SeqIO
import pandas as pd
records = SeqIO.parse("../../raw_data/conoserver/conoserver_230412_protein.fa", "fasta")
df = [[str(record.description), str(record.seq)] for record in records]
df = pd.DataFrame(df, columns=["description", "sequence"])
df["activity"] = df.description.str.contains("toxin")
df = df.replace(True, "toxic")
df = df.replace(False, None)
df = df[["sequence", "activity"]]
print(df)
df.to_csv("../../parsed_data/conoserver.csv", index=False)