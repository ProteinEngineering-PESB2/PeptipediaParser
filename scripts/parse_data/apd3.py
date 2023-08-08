from os import listdir
import pandas as pd
import os
from functions import verify_sequences
full_data = []
activity_replace = {"Anti-candida": "anti candida", "Anti-diabetes": "antidiabetic",
                    "Anti-endotoxin (sepsis related)": "anti endotoxin", "Anti-fungi": "antifungal",
                    "anti-Gram- ONLY": "anti gram negative", "anti-Gram+ ONLY": "anti gram positive",
                    "anti-Gram+_Gram- bacteria": "antibacterial", "Anti-HIV": "anti hiv",
                    "Anti-inflammatory": "anti inflammatory", "Anti-malaria (e": "anti malarian",
                    "Anti-MRSA": "anti mrsa", "Anti-parasites": "anti parasitic", "Anti-toxin": "anti toxin",
                    "Anti-tuberculosis (anti-TB)": "anti tubercular", "Anti-viruses": "antiviral", "AntiCancer": "anticancer",
                    "Antioxidant": "antioxidative", "Chemotaxis": "chemotactic", "Hemolytic peptides": "hemolytic",
                    "Insecticides": "insecticidal", "Ion channel inhibitors": "ion channel inhibitor", "Protease inhibitors": "protease inhibitor",
                    "Spermicides": "spermicide", "Surface immobilized peptides": "surface immobilized", "Synergistic AMPs": "antimicrobial",
                    "Two-chain AMPs": "antimicrobial", "Wound healing": "wound healing", "toxin": "toxic", "insecticide": "insecticidal"}

raw_folder = "../../raw_data/apd3/"
dfs = []
for filename in listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    a = pd.read_csv(path)
    a["activity"] = filename.split(".")[0]
    dfs.append(a)
df = pd.concat(dfs)
df = df.rename(columns={"1": "sequence"})
df = df[["sequence", "activity"]]
df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df.activity = df.activity.replace(activity_replace)
print(df)
df.to_csv("../../parsed_data/apd3.csv", index=False)