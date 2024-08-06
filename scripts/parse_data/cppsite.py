from Bio import SeqIO
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    records = SeqIO.parse(f"{raw_folder}/cppsite/natural_pep.fa", "fasta")
    sequences = [str(a.seq) for a in records]
    df = pd.DataFrame()
    df["sequence"] = sequences
    df["activity"] = "cell penetrating"
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/cppsite.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)