import os
import pandas as pd
from Bio import SeqIO
from utils import raw_folder, parse_df, parsed_folder
try:
    raw_folder = f"{raw_folder}/dbamp/"
    dfs = []
    for filename in os.listdir(raw_folder):
        if ".fasta" in filename:
            path = os.path.join(raw_folder, filename)
            a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
            a["activity"] = filename.replace(".fasta", "").replace("dbAMP_", "")
            dfs.append(a)
    df = pd.concat(dfs)
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/dbamp.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)