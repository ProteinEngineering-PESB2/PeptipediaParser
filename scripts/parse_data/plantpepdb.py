import pandas as pd
import os
from functions import verify_sequences

replace_dict = {"antihypertensive": "anti hypertensive", "anti-inflammatory": "anti inflammatory", "antioxidant": "antioxidative",
                "--na--": "", "antimalarial": "anti malarian", "antifeedant": "anti feedant", "toxin": "toxic",
                "antiproliferative": "anti proliferative", "anti-hiv": "anti hiv", "antibiofilm": "anti biofilm", "ace-inhibitor": "ace inhibitor",
                "antiparasitic": "anti parasitic", "alpha-amylase-inhibitor": "alpha-amylase inhibitor", "celiac-toxic": "celiac toxic",
                "defense-gene-activator": "defense gene activator", "tyrosinase-inhibitor": "tyrosinase inhibitor",
                "uterotonic-activity": "uterotonic", "protease-inhibitor": "protease inhibitor", "hmg-coa-reductase-inhibitor": "hmg-coa reductase inhibitor",
                "cell-growth-inhibitor": "cell growth inhibitor", "development-regulator": "development regulator", "enzyme-inhibitor": "enzyme inhibitor",
                "nematocide": "anti nematode", "opioid-agonist": "opioid agonist", "opioid-antagonist": "opioid antagonist"}

dfs = []
raw_folder = "../../raw_data/plantpepdb/"
path = raw_folder + "plantpepdb.csv"
df = pd.read_csv(path)
df = df[["sequence", "Peptide Activity"]]
df = df.rename(columns={"Peptide Activity": "activity"})
df["activity"] = df.activity.str.split(", ")
df = df.explode("activity")
df.activity = df.activity.str.lower()
df.activity = df.activity.replace(replace_dict)
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/plantpepdb.csv", index=False)