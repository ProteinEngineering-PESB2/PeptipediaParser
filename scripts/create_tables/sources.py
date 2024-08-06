"""Assign source to peptide"""
import pandas as pd

peptipedia_data = pd.read_csv("../../output/all_data.csv") #Reads all data
sources = peptipedia_data[["source"]].drop_duplicates().reset_index(drop=True)
sources["id_source"] = sources.index + 1
sources = sources.rename(columns={"source": "name"})
urls = pd.read_csv("../../auxiliar_data/source_descriptions.csv") #Info about source

sources = sources.merge(urls, on="name", how="left")
sources.to_csv("../../tables/source.csv", index=False) #Sources table

#Relationship between peptide and source
peptipedia_data = peptipedia_data.merge(sources, left_on="source", right_on="name")
phs = peptipedia_data[["id_sequence", "id_source"]].drop_duplicates()
phs = phs.rename(columns={"id_sequence": "id_peptide"})
phs.to_csv("../../tables/peptide_has_source.csv", index=False)
