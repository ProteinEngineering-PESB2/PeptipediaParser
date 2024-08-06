"""B3Pred"""
import os
from Bio import SeqIO
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
try:
    raw_folder = f"{raw_folder}/qsppred/"
    dfs = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        df = pd.DataFrame([[str(a.seq)]
                       for a in list(SeqIO.parse(path, "fasta"))],
                       columns=["sequence"])
        dfs.append(df)
    df = pd.concat(dfs)
    df["activity"] = "quorum_sensing"
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/qsppred.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)