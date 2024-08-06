import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    raw_folder = f"{raw_folder}/dravp/"
    df = pd.read_excel(f"{raw_folder}antiviral_peptides.xlsx")
    df = df[["Sequence", "Target_Organism", "Pubmed_ID"]]
    df["activity"] = df.Target_Organism.str.split(",")
    df = df.explode("activity")
    df.activity = df.activity.str.strip()
    df = df.rename(columns={"Sequence": "sequence", "Pubmed_ID": "pubmed"}).drop(columns=["Target_Organism"])
    df = df.drop_duplicates()
    df = parse_df(df)
    df = df.reset_index(drop=True)
    df["activity"] = "anti " + df["activity"]
    df.pubmed = df.pubmed.str.split("##")
    df = df.explode("pubmed")
    df.to_csv(f"{parsed_folder}/dravp.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)