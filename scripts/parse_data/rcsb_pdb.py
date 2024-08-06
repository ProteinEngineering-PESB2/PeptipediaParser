import pandas as pd
from Bio import SeqIO
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    pdb_path = f"{raw_folder}/rcsb_pdb/pdb_seqres.txt"
    df = pd.DataFrame([[a.description, str(a.seq)] for a in list(SeqIO.parse(pdb_path, "fasta"))], columns=["id", "sequence"])
    df = df[df.id.str.contains("protein")]
    df = df[["sequence"]]
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/rcsb_pdb.csv", index=False)

    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)