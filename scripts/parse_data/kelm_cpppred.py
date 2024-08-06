import os
from Bio import SeqIO
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
try:
    path = f"{raw_folder}/kelm-cpppred/Dataset/Independent-dataset/pos.fasta"
    df = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
    df["activity"] = "cell penetrating"
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/kelm-cpppred.csv", index=False)

    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)