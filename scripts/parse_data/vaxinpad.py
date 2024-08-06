import pandas as pd
from Bio import SeqIO
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    filename = f"{raw_folder}/vaxinpad/Immunomodulatory Peptides (A-cell epitopes).txt"
    with open(filename, mode="r", encoding="utf-8") as file:
        text = file.read()
    text_splitted = text.split()
    df = pd.DataFrame()
    df["sequence"] = text_splitted
    df["activity"] = "immunomodulatory"
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/vaxinpad.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)