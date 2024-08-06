from os import listdir
from Bio import SeqIO
import pandas as pd
import os
from utils import parse_df, raw_folder, parsed_folder
try:
    full_data = []
    raw_folder = f"{raw_folder}/amp/"
    dfs = []
    for filename in listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        a = pd.DataFrame([[str(a.seq)]
                          for a in list(SeqIO.parse(path, "fasta"))],
                         columns=["sequence"])
        a["activity"] = "antimicrobial"
        dfs.append(a)
    df = pd.concat(dfs)
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/amp.csv", index=False)

    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)