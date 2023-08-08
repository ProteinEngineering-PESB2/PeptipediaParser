from os import listdir
from Bio import SeqIO
import pandas as pd
import os
from functions import verify_sequences
full_data = []
raw_folder = "../../raw_data/ampfun/"
dfs = []
replace_dict = {
    "stage1": "antimicrobial",
    "stage2_fungal": "antifungal",
    "stage2_gram_neg": "anti gram negative",
    "stage2_gram_pos": "anti gram positive",
    "stage2_mammalian": "anti mammalian cell",
    "stage2_parasitic": "anti parasitic",
    "stage2_viral": "antiviral"
}
for filename in listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
    a["activity"] = filename.replace(".fasta", "").replace("_test_pos", "").replace("_train_pos", "")
    dfs.append(a)
df = pd.concat(dfs)
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df["activity"] = df.activity.replace(replace_dict, regex=True)
print(df)
df.to_csv("../../parsed_data/ampfun.csv", index=False)