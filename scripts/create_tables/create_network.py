import pandas as pd
import re
import networkx as nx

def create():
    with open("../../auxiliar_data/tree.tsv", encoding="utf-8", mode = "r") as file:
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
                sub_levels = levels.iloc[:i]
                brother = sub_levels[sub_levels.level == row.level].act.values[-1]
                parent = [obj["parent"] for obj in data if obj["child"] == brother]
                data.append({
                    "parent": parent[0],
                    "child": row.act
                })
    df = pd.DataFrame(data)
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row.parent, row.child)
    return G