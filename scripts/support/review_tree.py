"""Review tree consistency"""
import pandas as pd
import re

parsed_data_folder = "../../parsed_data"
aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"


data = pd.read_csv(f"{output_folder}/all_data.csv")
activities = data[data.activity.notna()][["activity"]].drop_duplicates()
with open(f"{aux_data_folder}/tree.tsv", encoding="utf-8", mode = "r") as file:
    tree_text = file.read().splitlines()
data = []

for i, row in enumerate(tree_text):
    level = len(re.findall('\t', row))
    act = row.strip()
    data.append({"level": level, "act": act})
levels = pd.DataFrame(data)
a = levels.merge(activities, right_on="activity", left_on="act", how="outer")
a.to_csv(f"{output_folder}/reviewed_tree.csv", index=False) #Review tree file
