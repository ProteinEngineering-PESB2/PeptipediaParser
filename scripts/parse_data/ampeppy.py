from Bio import SeqIO
import pandas as pd
import os
from utils import parse_df, raw_folder, parsed_folder
try:
    raw_folder = f"{raw_folder}/ampeppy/"
    filename = "M_model_train_AMP_sequence.numbered.fasta"
    path = os.path.join(raw_folder, filename)
    df = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
    df["activity"] = "antimicrobial"
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/ampeppy.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)