import pandas as pd
import os
from utils import raw_folder, parse_df, parsed_folder
def verify_pubmed(text):
    try:
        text = int(text)
        if text > 1000:
            return text
    except:
        return None
try:
    data = []
    df = pd.read_csv(f"{raw_folder}/camp/CAMP_2023-05-26 20-14-20.txt", sep="\t")
    df = df[["Activity", "Gram_Nature", "Seqence", "Pubmed_id"]]
    df = df.drop_duplicates()
    df["Activity"] = df["Activity"].str.replace(" ", "").str.split(",")
    df["Gram_Nature"] = df["Gram_Nature"].str.replace(" ", "").str.split(",")
    df = pd.concat([
        df[["Seqence", "Activity", "Pubmed_id"]],
        df[["Seqence", "Gram_Nature", "Pubmed_id"]].rename(columns = {"Gram_Nature": "Activity"})
    ])
    df = df.explode("Activity")
    df = df.rename(columns={"Seqence": "sequence", "Activity": "activity", "Pubmed_id": "pubmed"})
    df.activity = df.activity.str.split(".")
    df = df.explode("activity")
    df = df.dropna(subset=["sequence"])
    df.pubmed = df.pubmed.str.split(", ")
    df = df.explode("pubmed")
    df.pubmed = df.pubmed.str.strip()
    df.pubmed = df.pubmed.map(verify_pubmed)
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/camp.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)
