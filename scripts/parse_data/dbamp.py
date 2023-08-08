import os
import pandas as pd
from Bio import SeqIO
from functions import verify_sequences
replace_dict = {"mammaliancells": "anti mammalian cell", "cellpenetrating": "cell penetrating", "mollicute": "anti mollicute",
                "mastcelldegranulating": "mast cell degranulating", "plasmaanticlotting": "plasma anti clotting", "woundhealing": "wound healing",
                "edemainducer": "edema inducer", "surfaceimmobilized": "surface immobilized", "anti,gram_p": "anti gram positive", "antioxidant": "antioxidative",
                "antigram_n": "anti gram negative", "antihypertensive": "anti hypertensive", "antiinflammatory": "anti inflammatory", "antigram_p": "anti gram positive",
                "antiangiogenesis": "anti angiogenic", "antihiv": "anti hiv", "antimalarial": "anti malarian", "antinematode": "anti nematode", "antimrsa": "anti mrsa", "cytotoxin": "cytotoxic", "enzymeinhibitor": "enzyme inhibitor",
                "anurandefense": "anuran defense", "antitumour": "antitumor", "antiparasitic": "anti parasitic", "antibiofilm": "anti biofilm", "spermicidal": "spermicide"}

raw_folder = "../../raw_data/dbamp/"
dfs = []
for filename in os.listdir(raw_folder):
    if ".fasta" in filename:
        path = os.path.join(raw_folder, filename)
        a = pd.DataFrame([[str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["sequence"])
        a["activity"] = filename.replace(".fasta", "").replace("dbAMP_", "").lower()
        dfs.append(a)
df = pd.concat(dfs)
df = df.replace(replace_dict)
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df.activity = df.activity.replace(replace_dict)
print(df)
df.to_csv("../../parsed_data/dbamp.csv", index=False)