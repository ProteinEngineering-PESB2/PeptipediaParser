"""Simply count things"""
import pandas as pd

aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"


df = pd.read_csv(f"{output_folder}/all_data_post_tree_act.csv")
acts = df.drop_duplicates(subset=["id_sequence", "activity"])
acts = acts.value_counts(subset="activity")
acts.to_csv(f"{output_folder}/activities_count.csv") #Counts activities

df = pd.read_csv(f"{output_folder}/all_data_post_tree.csv")

src = df.drop_duplicates(subset=["id_sequence", "source"])
src = src.value_counts(subset="source")
src.to_csv(f"{output_folder}/sources_count.csv") #Counts sources