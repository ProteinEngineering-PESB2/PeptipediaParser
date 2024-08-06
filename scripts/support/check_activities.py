"""Checks if there is any duplicate in activity_replacement.csv"""
import pandas as pd

parsed_data_folder = "../../parsed_data"
aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"

activities = pd.read_csv(f"{aux_data_folder}/activity_replacement.csv")
all_data = pd.read_csv(f"{output_folder}/all_data.csv")

replacements = all_data[["keyword", "activity"]].drop_duplicates()
print(replacements)
replacements.to_csv(f"{aux_data_folder}/replacements.csv", index=False) #replacements shouldn't has nulls