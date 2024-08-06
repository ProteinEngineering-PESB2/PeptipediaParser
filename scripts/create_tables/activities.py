import pandas as pd

import networkx as nx
from create_network import create

G = create()

activities = pd.read_csv("../../output/activities_count.csv") #Counts tables
activities = activities.rename(columns={"activity": "name"})[["name"]]

activities["id_activity"] = activities.index + 1

descriptions = pd.read_csv("../../auxiliar_data/activity_descriptions.csv", sep="|") #Descriptions
descriptions = descriptions.rename(columns={"activity": "name"})[["name", "description"]]

activities = activities.merge(descriptions, on="name", how="left")

paths = []
#Obtains id_parents
for i in list(G.nodes)[1:None:None]:
    path= nx.dijkstra_path(G, i, 'All activities')
    parent = path[1]
    paths.append({"name": i , "parent": parent})

parents = pd.DataFrame(paths)
a = parents.merge(activities, left_on="parent", right_on="name")[["parent", "id_activity"]].drop_duplicates().rename(columns={"id_activity": "id_parent"})
parents = parents.merge(a, on="parent")[["name", "id_parent"]] #activity, id_parent
activities = activities.merge(parents, on="name", how="left")
activities.to_csv("../../tables/activity.csv", index=False) #Table activity

#Obtains relationship between peptide and activity
pivoted = pd.read_csv("../../output/activities_pivoted.csv")
pivoted = pivoted.rename(columns={"id_sequence": "id_peptide"})
pivoted = pivoted.drop(columns=["sequence"])

melted = pivoted.melt(id_vars=["id_peptide"], var_name="activity")
melted = melted[melted.value == 1][["id_peptide", "activity"]]
melted = melted.merge(activities, left_on="activity",
                      right_on="name")[["id_peptide", "id_activity"]].drop_duplicates()
melted["predicted"] = False #Reported activities in peptides

melted.to_csv("../../tables/peptide_has_activity.csv", index=False) #Peptide has activity table