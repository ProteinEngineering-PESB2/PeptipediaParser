from Bio import SeqIO
import pandas as pd
from os import listdir
from config import *
from os.path import basename
import os

script_name = basename(__file__.split(".")[0])
full_data = []
raw_folder = RAW_FOLDER.format(script_name)
dfs = []
for filename in listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    dfs.append(pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path,"fasta"))], columns=["sequence"]))
df = pd.concat(dfs)
df["activity"] = "antimicrobial"
print(df)
df.to_csv(os.path.join(PARSED_FOLDER, script_name + ".csv"), index=False)