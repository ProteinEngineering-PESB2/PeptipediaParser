from Bio import SeqIO
import pandas as pd
import os
from functions import verify_sequences

raw_folder = "../../raw_data/ampeppy/"
filename = "M_model_train_AMP_sequence.numbered.fasta"
path = os.path.join(raw_folder, filename)
df = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
df["activity"] = "antimicrobial"
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv(os.path.join("../../parsed_data/ampeppy.csv"), index=False)
