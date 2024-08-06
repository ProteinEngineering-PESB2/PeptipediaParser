import pandas as pd
from Bio import SeqIO
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    raw_folder = f"{raw_folder}/iacp-drlf/"
    a = [[str(a.seq), a.description.split("|")[-1]] for a in list(SeqIO.parse(f"{raw_folder}/ACP20AltTest.fasta", "fasta"))]
    b = [[str(a.seq), a.description.split("|")[-1]] for a in list(SeqIO.parse(f"{raw_folder}/ACP20AltTrain.fasta", "fasta"))]
    c = [[str(a.seq), a.description.split("|")[-1]] for a in list(SeqIO.parse(f"{raw_folder}/ACP20mainTest.fasta", "fasta"))]
    d = [[str(a.seq), a.description.split("|")[-1]] for a in list(SeqIO.parse(f"{raw_folder}/ACP20mainTrain.fasta", "fasta"))]
    a = pd.DataFrame(a, columns=["sequence", "activity"])
    b = pd.DataFrame(b, columns=["sequence", "activity"])
    c = pd.DataFrame(c, columns=["sequence", "activity"])
    d = pd.DataFrame(d, columns=["sequence", "activity"])
    df = pd.concat([a, b, c, d])
    df = df[df.activity == "1"]
    df = df.replace("1", "anticancer")
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    
    df.to_csv(f"{parsed_folder}/iacp-drlf.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)