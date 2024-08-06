import pandas as pd
from Bio import SeqIO
from utils import raw_folder, parse_df, parsed_folder
import os

try:
    raw_folder = f"{raw_folder}/ensemble_amppred/AMP_data_for_download/"
    sequences = []
    for filename in os.listdir(raw_folder):
        if "AMP" in filename and "Non" not in filename:
            sequences += [str(a.seq) for a in SeqIO.parse(f"{raw_folder}/{filename}", format="fasta")]
    df = pd.DataFrame()
    df["sequence"] = sequences
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df["activity"] = "antimicrobial"
    df.to_csv(f"{parsed_folder}/ensemble_amppred.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)