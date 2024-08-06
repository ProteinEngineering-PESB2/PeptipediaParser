"""APIN"""
import os
import pandas as pd
from utils import raw_folder, parsed_folder, parse_df
from Bio import SeqIO
try:
    raw_folder = f"{raw_folder}/apin/"
    dfs = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        data = pd.DataFrame([[str(a.seq)]
                            for a in list(SeqIO.parse(path, "fasta"))],
                            columns=["sequence"])
        data["activity"] = "antimicrobial"
        data = data.rename(columns={0: "sequence"})
        dfs.append(data)
    df = pd.concat(dfs)
    df = parse_df(df)

    df.to_csv(os.path.join(f"{parsed_folder}/apin.csv"), index=False)

    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)