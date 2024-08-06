"""Bactibase"""
import os
from Bio import SeqIO
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
try:
    df = pd.read_csv(f"{raw_folder}/bactibase/bactibase.csv")
    swissprot = f"{raw_folder}/swissprot/uniprot_sprot.fasta"
    swissprot = pd.DataFrame([[a.id.split("|")[1], str(a.seq)] for a in list(SeqIO.parse(swissprot, "fasta"))], columns=["id", "sequence"])
    df = df.merge(swissprot, left_on="UniProt", right_on="id")
    df = df[["sequence"]]
    df["activity"] = "antibacterial"
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/bactibase.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)
