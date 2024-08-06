import pandas as pd
from Bio import SeqIO
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    train = [str(a.seq) for a in SeqIO.parse(f"{raw_folder}/preaip/test-positive.txt", format="fasta")]
    test = [str(a.seq) for a in SeqIO.parse(f"{raw_folder}/preaip/training-positive.txt", format="fasta")]
    sequences = train + test
    df = pd.DataFrame()
    df["sequence"] = sequences
    df["activity"] = "anti inflammatory"
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/preaip.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)