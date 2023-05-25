from Bio import SeqIO
import pandas as pd
from os import makedirs
parsed_folder = "../../parsed_data/"
records = SeqIO.parse("../../raw_data/swissprot/uniprot_sprot.fasta", "fasta")
data = [[str(a.seq), str(a.id).split("|")[1]] for a in records]
df = pd.DataFrame(data, columns=["sequence", "id"])
print(df)
df.to_csv(f"{parsed_folder}/swissprot.csv", index=False)