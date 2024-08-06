from os import listdir
from Bio import SeqIO
import pandas as pd
from utils import get_patent, parsed_folder, raw_folder, parse_df
import os
def get_pubmed(text):
    if "pubmed" in text:
        return text.split("/pubmed/")[1][:-1]
try:
    full_data = []
    raw_folder = f"{raw_folder}/antiangiopred/"
    dfs = []
    for filename in listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        a = pd.DataFrame([[str(a.seq), a.description] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence", "description"])
        a["activity"] = "anti angiogenic"
        dfs.append(a)
    df = pd.concat(dfs)
    df["patent"] = df.description.map(get_patent)
    df["pubmed"] = df.description.map(get_pubmed)
    df = df.drop(columns=["description"])
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/antiangiopred.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)