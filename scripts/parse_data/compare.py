from Bio import SeqIO
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    parsed_folder = f"{parsed_folder}/"
    records = SeqIO.parse(f"{raw_folder}/compare/COMPARE-2023-FastA-Seq.txt", "fasta")
    data = [[str(a.seq)] for a in records]
    df = pd.DataFrame(data, columns=["sequence"])
    df["activity"] = "allergen"
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/compare.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)