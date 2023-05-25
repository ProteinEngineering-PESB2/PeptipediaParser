from Bio import SeqIO
import pandas as pd
from config import *
from os.path import basename
import os

script_name = basename(__file__.split(".")[0])
full_data = []
raw_folder = RAW_FOLDER.format(script_name)

for filename in os.listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    data = [[str(a.seq), a.description.split("|")[1]]
            for a in list(
                SeqIO.parse(path, "fasta"))]
    df = pd.DataFrame(data, columns=["sequence", "activity"])
    full_data.append(df)
df = pd.concat(full_data)
df = df[df.activity == "1"]
df["activity"] = "anticancer"
print(df)
df.to_csv(os.path.join(PARSED_FOLDER, script_name + ".csv"), index=False)