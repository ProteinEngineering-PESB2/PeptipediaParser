import pandas as pd
from os import listdir
from Bio import SeqIO
import pandas as pd
import os
from functions import verify_sequences

full_data = []
raw_folder = "../../raw_data/arachnoserver/"
dfs = []
for filename in listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
    a["activity"] = filename.split(".")[0]
    dfs.append(a)
df = pd.concat(dfs)
replace_dict = {
    'Activity not known': None, "all": None
}
df.activity = df.activity.replace(replace_dict).str.lower().str.replace(" ", "-")

df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df.activity = df.activity.replace({"antiparasitic": "anti parasitic"})
print(df)
df.to_csv("../../parsed_data/arachnoserver.csv", index=False)