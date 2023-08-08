import os
from Bio import SeqIO
import pandas as pd
from functions import verify_sequences
path = "../../raw_data/lamp2/lamp2.fasta"
df = pd.DataFrame([[str(a.id.split("|")[0]),str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["id","sequence"])

df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
activities = pd.read_csv("../../raw_data/lamp2/lamp2_activities.csv")
df = df.merge(activities, how="left")
df = df[["sequence", "activity", "is_canon"]]
df.activity = df.activity.replace({None: "antimicrobial", "antiparasitic": "anti parasitic"})
print(df)
df.to_csv("../../parsed_data/lamp2.csv", index=False)