import os
import pandas as pd
import re
import networkx as nx

with open("./tree.txt", encoding="utf-8", mode = "r") as file:
    tree_text = file.read().splitlines()
data = []

for i, row in enumerate(tree_text):
    level = len(re.findall('\t', row))
    act = row.strip()
    data.append({"level": level, "act": act})
levels = pd.DataFrame(data)
data = []
for i, row in levels.iterrows():
    if i > 0:
        if row.level > levels.iloc[i - 1].level:
            data.append({
                "parent": levels.iloc[i - 1].act,
                "child": row.act
            })
        elif row.level == levels.iloc[i - 1].level:
            data.append({
                "parent": data[-1]["parent"],
                "child": row.act
            })
        elif row.level < levels.iloc[i - 1].level:
            brother = levels[levels.level == row.level].act.values[0]
            parent = [obj["parent"] for obj in data if obj["child"] == brother]
            data.append({
                "parent": parent[0],
                "child": row.act
            })
df = pd.DataFrame(data)
G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row.parent, row.child)

parsed_folder = "../parsed_data/"
dfs = []
for file in os.listdir(parsed_folder):
    path = os.path.join(parsed_folder, file)
    db = pd.read_csv(path)
    db["source"] = file.split(".")[0]
    dfs.append(db)
df = pd.concat(dfs)
df = df.replace("-", " ", regex=True)
df = df.replace(r"\s+", " ", regex=True)
df["sequence"] = df["sequence"].replace("", None)
df["activity"] = df["activity"].replace("", None)
replacement = pd.read_csv("./activity_replacement.csv")
df = df.merge(replacement, on="activity", how="outer").drop(columns=["activity"]).rename(columns={"Proposal activity": "activity"})
df = df.dropna(subset=["sequence"])
sequences = df[["sequence", "is_canon"]].drop_duplicates().reset_index(drop=True)
sequences["id"] = sequences.index + 1
sequences = sequences[["id", "sequence", "is_canon"]]
sequences.to_csv("../output/all_peptides.csv", index=False)
sequences = sequences.drop(columns=["is_canon"])
###
df = df.merge(sequences, on="sequence")
df = df[["id", "sequence", "activity", "source", "is_canon"]]
df.to_csv("../output/peptipedia_data.csv", index=False)
###
a = df[["sequence", "source"]].drop_duplicates()
sources = a.value_counts(subset=["source"])
sources = sources.sort_values(ascending=False)
sources.to_csv("../output/sources_count.csv", index=True)

###
a = df[["sequence", "activity"]].drop_duplicates().dropna()
for i in G.nodes():
    path = nx.dijkstra_path(G, i, 'All activities')[:-1]
    a.loc[a.activity == str(i), "activity"] = [path]
a = a.explode("activity").drop_duplicates()
activities = a.value_counts(subset=["activity"])
activities = activities.sort_values(ascending=False)
activities.to_csv("../output/activities_count.csv", index=True)

###
""" a = df[["id", "sequence", "activity", "is_canon"]].drop_duplicates()
a = a.dropna() """
a["value"] = 1
a = a.pivot(index=["sequence"], columns="activity", values="value")
a = a.fillna(0)
a.to_csv("../output/activity_pivoted.csv", index=True)
