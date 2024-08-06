"""AMP SCAN 2"""
import os
from Bio import SeqIO
import pandas as pd
from utils import verify_sequences, raw_folder, parsed_folder
try:
    full_data = []
    raw_folder = f"{raw_folder}/amp_scan_2/"
    dfs = []
    for filename in os.listdir(raw_folder):
        if "AMP" in filename and ".fa" in filename:
            path = os.path.join(raw_folder, filename)
            a = pd.DataFrame([[str(a.seq)]
                            for a in list(SeqIO.parse(path, "fasta"))],
                            columns=["sequence"])
            a["activity"] = "antimicrobial"
            dfs.append(a)
    df = pd.concat(dfs)
    df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
    df = df.dropna(subset=["sequence"])
    df = df.drop_duplicates()
    df.to_csv(f"{parsed_folder}/amp_scan_2.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)