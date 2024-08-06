import os
from Bio import SeqIO
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
try:
    path = f"{raw_folder}/lamp2/lamp2.fasta"
    df = pd.DataFrame([[str(a.id.split("|")[0]),str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["id","sequence"])

    df = parse_df(df)
    activities = pd.read_csv(f"{raw_folder}/lamp2/lamp2_activities.csv")
    df = df.merge(activities, how="left")
    df = df[["sequence", "activity", "is_canon"]]
    df.activity = df.activity.replace({None: "antimicrobial", "antiparasitic": "anti parasitic"})
    df.to_csv(f"{parsed_folder}/lamp2.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)