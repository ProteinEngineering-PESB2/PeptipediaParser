"""Converts activities predicted table to Pivoted table"""
import pandas as pd

output_folder = "../../output"
tables_folder = "../../tables"

df = pd.read_csv(f"{tables_folder}/peptide_has_activity.csv")
df = df[df.predicted].drop(columns="predicted")
activity = pd.read_csv(f"{tables_folder}/activity.csv")[["id_activity", "name"]]
peptide = pd.read_csv(f"{tables_folder}/peptide.csv")[["id_peptide", "sequence", "is_canon"]]

df = df.merge(activity, on="id_activity")
df["values"] = 1
df = df.pivot_table(index="id_peptide", columns="name", values="values", fill_value = 0)
df["id_peptide"] = df.index
df = df.reset_index(drop=True)
df = df.merge(peptide, on="id_peptide")
df.to_csv(f"{output_folder}/predicted_activities_pivoted.csv", index=False)