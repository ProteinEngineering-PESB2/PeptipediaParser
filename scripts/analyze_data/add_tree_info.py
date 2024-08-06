"""Adds info about parents and childs activites"""
import pandas as pd
import networkx as nx
import numpy as np
from create_network import create

aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"

G = create() #Graph
df = pd.read_csv(f"{output_folder}/all_data.csv")

a = df[["activity"]].drop_duplicates().dropna()
paths = []
for i in G.nodes():
    if i != "All activities":
        path = nx.dijkstra_path(G, i, 'All activities')[:-1]
        paths.append({"activity": str(i), "path": path})
#Gets parents, grandparents, grandgrandparents, etc...

paths = pd.json_normalize(paths).explode("path")
df = df.merge(paths, on="activity", how="left")
df = df.drop_duplicates()
df = df.drop(columns=["activity"])
df = df.rename(columns={"path": "activity"})

df.to_csv(f"{output_folder}/all_data_post_tree.csv", index=False)
df = df[df.activity.notna()]
df.to_csv(f"{output_folder}/all_data_post_tree_act.csv", index=False) #Only with activities 