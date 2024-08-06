import os
import pandas as pd
from Bio import SeqIO
from utils import raw_folder, parse_df, parsed_folder
try:
    raw_folder = f"{raw_folder}/ennavia"
    dfs = []
    for file in os.listdir(raw_folder):
        path = os.path.join(raw_folder, file)
        a = pd.DataFrame([[str(a.seq), a.id.split("|")[3]] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence", "activity"])
        a = a[~a.activity.str.contains("non")]
        dfs.append(a)
    df = pd.concat(dfs)
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/ennavia.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)