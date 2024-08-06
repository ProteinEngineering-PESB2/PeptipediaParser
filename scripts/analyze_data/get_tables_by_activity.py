"""Tables requested for to build predictive models"""
import pandas as pd


aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"

data = pd.read_csv(f"{output_folder}/all_data_post_tree_act.csv")
for act in data.activity.unique():
    print(act)
    a = data[data.activity == act][["id_sequence", "sequence", "is_canon"]].drop_duplicates()
    a.to_csv(f'{output_folder}/tables_activities/{act.replace(" ", "_")}.csv', index=False)


data = pd.read_csv(f"{output_folder}/all_data_non_act.csv")
data = data[["id_sequence", "sequence", "is_canon"]].drop_duplicates()
data.to_csv(f'{output_folder}/without_activity/sequences.csv', index=False)
