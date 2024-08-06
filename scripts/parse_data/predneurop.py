import pandas as pd
from Bio import SeqIO
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    raw_folder = f"{raw_folder}/predneurop/"
    sequences = []
    for filename in os.listdir(raw_folder):
        sequences += [str(a.seq) for a in SeqIO.parse(f"{raw_folder}/{filename}", format="fasta")]

    df = pd.DataFrame()
    df["sequence"] = sequences
    df["activity"] = "neuropeptide"
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/predneurop.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)