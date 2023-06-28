import pandas as pd
from functions import verify_sequences
import os
from Bio import SeqIO
replace_dict  = {"Biofilm" : "anti biofilm", "Cancer": "anticancer", "Fungus": "antifungal",
                 "Gram-": "anti gram negative", "Gram+": "anti gram positive", "Insect": "anti insect",
                 "Mammalian Cell": "anti mammalian cell", "Mollicute": "anti mollicute", "Nematode": "anti nematode",
                 "Parasite": "anti parasitic", "Protista": "anti protista", "Virus": "antiviral"}
raw_folder = "../../raw_data/dbaasp/"
datas = []
for filename in os.listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    records = SeqIO.parse(path, "fasta")
    df = [[str(record.seq)] for record in records]
    df = pd.DataFrame(df, columns=["sequence"])
    df["activity"] = filename.split(".")[0]
    datas.append(df)
df = pd.concat(datas)
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df = df.replace(replace_dict)
print(df)
df.to_csv("../../parsed_data/dbaasp.csv", index=False)