from os import listdir
import pandas as pd
import os
from functions import verify_sequences
full_data = []
activity_replace = {"Anti-candida": "antifungal", "Anti-diabetes": "antidiabetic",
                    "Anti-endotoxin (sepsis related)": "antiendotoxin", "Anti-fungi": "antifungal",
                    "anti-Gram- ONLY": "anti gram-negative", "anti-Gram+ ONLY": "anti gram-positive",
                    "anti-Gram+_Gram- bacteria": "antibacterial", "Anti-HIV": "antihiv",
                    "Anti-inflammatory": "antiinflammatory", "Anti-malaria (e": "antimalarian",
                    "Anti-MRSA": "anti-mrsa", "Anti-parasites": "antiparasitic", "Anti-toxin": "antitoxin",
                    "Anti-tuberculosis (anti-TB)": "antitubercular", "Anti-viruses": "antiviral", "AntiCancer": "anticancer",
                    "Antioxidant": "antioxidant", "Chemotaxis": "chemotaxis", "Hemolytic peptides": "hemolytik",
                    "Insecticides": "insecticide", "Ion channel inhibitors": "ion channel inhibitor", "Protease inhibitors": "protease inhibitor",
                    "Spermicides": "spermicide", "Surface immobilized peptides": "surface immobilized", "Synergistic AMPs": "antimicrobial",
                    "Two-chain AMPs": "antimicrobial", "Wound healing": "wound healing"}

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
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
df = df.replace(activity_replace)
print(df)
df.to_csv("../../parsed_data/apd3.csv", index=False)