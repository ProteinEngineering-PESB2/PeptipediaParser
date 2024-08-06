"""Converts to One Hot or Pivoted table"""
import pandas as pd

parsed_data_folder = "../../parsed_data"
aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"

df = pd.read_csv(f"{output_folder}/all_data_post_tree_act.csv")
df = df[["id_sequence", "is_canon", "sequence", "activity"]].drop_duplicates()
df["values"] = 1
pivoted = df.pivot(index=["id_sequence", "is_canon", "sequence"], columns=["activity"], values=["values"])
pivoted = pivoted.fillna(0)
pivoted.columns = pivoted.columns.droplevel(0)
pivoted = pivoted.reset_index().rename_axis(None, axis=1)

pivoted.to_csv(f"{output_folder}/activities_pivoted.csv", index=False)