from Bio import SeqIO
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(f"{raw_folder}/deepacp/ACPs10.txt", "fasta"))], columns=["sequence"])
    b = pd.DataFrame([[str(b.seq)] for b in list(SeqIO.parse(f"{raw_folder}/deepacp/ACPs82.txt", "fasta"))], columns=["sequence"])
    c = pd.DataFrame([[str(c.seq)] for c in list(SeqIO.parse(f"{raw_folder}/deepacp/ACPs250.txt", "fasta"))], columns=["sequence"])
    df = pd.concat([a, b, c])
    df["activity"] = "anticancer"
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/deepacp.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)