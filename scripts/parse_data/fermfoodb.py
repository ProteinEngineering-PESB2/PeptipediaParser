import os
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
def filter_pubmed(text):
    try:
        int(text)
        return text
    except:
        return None
try:
    raw_folder = f"{raw_folder}/fermfoodb/"
    dfs = []
    for file in os.listdir(raw_folder):
        path = os.path.join(raw_folder, file)
        df = pd.read_csv(path)
        dfs.append(df)
    df = pd.concat(dfs)
    df = df[["PubMed ID","Peptide_Sequence", "Activity"]]
    df = df.rename(columns={"PubMed ID": "pubmed", "Peptide_Sequence": "sequence", "Activity": "activity"})
    
    df.pubmed = df.pubmed.str.split(";")
    df = df.explode("pubmed")
    df.pubmed = df.pubmed.str.strip()
    df.activity = df.activity.str.split(";")
    df = df.explode("activity")
    df.activity = df.activity.str.strip()
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df2 = df.copy()
    df2.activity = "Nutraceutical"
    df = pd.concat([df, df2])
    df.pubmed= df.pubmed.map(filter_pubmed)
    df.to_csv(f"{parsed_folder}/fermfoodb.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)