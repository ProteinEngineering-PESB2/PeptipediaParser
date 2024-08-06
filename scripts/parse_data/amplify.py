import os
from Bio import SeqIO
import pandas as pd
from utils import parsed_folder, raw_folder, parse_df
try:
    full_data = []
    raw_folder = f"{raw_folder}/amplify/"
    dfs = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        a = pd.DataFrame([[str(a.seq)]
                          for a in list(SeqIO.parse(path, "fasta"))],
                          columns=["sequence"])
        a["activity"] = "antimicrobial"
        dfs.append(a)
    df = pd.concat(dfs)
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/amplify.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)