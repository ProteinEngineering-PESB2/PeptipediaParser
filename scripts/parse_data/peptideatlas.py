import os
import pandas as pd
from Bio import SeqIO
from utils import raw_folder, parse_df, parsed_folder
try:
    df = pd.DataFrame()
    sequences_total = []
    for file in os.listdir(f"{raw_folder}/peptideatlas/"):
        records = SeqIO.parse(f"{raw_folder}/peptideatlas/{file}", "fasta")
        sequences = [str(a.seq) for a in records]
        sequences_total += sequences
    df["sequence"] = sequences_total
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/peptideatlas.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)