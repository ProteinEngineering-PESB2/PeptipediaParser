import pandas as pd
import os
from Bio import SeqIO
from utils import raw_folder, parse_df, parsed_folder

try:
    dfs = []
    raw_folder = f"{raw_folder}/dramp/"
    for file in os.listdir(raw_folder):
        path = os.path.join(raw_folder, file)
        a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
        a["activity"] = file.replace("_amps.fasta", "")
        dfs.append(a)
    df = pd.concat(dfs)
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/dramp.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)