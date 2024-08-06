"""Adds cite to all data"""
import pandas as pd

def combine_citation(doi, pubmed):
	if pubmed is not None:
		return pubmed
	elif doi is not None:
		return doi
aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"

df = pd.read_csv(f"{output_folder}/all_data.csv")
df.pubmed = df.pubmed.astype(str)
df.pubmed = df.pubmed.str.replace(".0", "")
pubmeds = pd.read_csv(f"{aux_data_folder}/pubmeds.csv")
pubmeds.pubmed = pubmeds.pubmed.astype(str)
dois = pd.read_csv(f"{aux_data_folder}/dois.csv")
df = df.merge(pubmeds, on="pubmed", how="left")
df = df.merge(dois, on="doi", how="left")

df["citation"] = df.apply(lambda x: combine_citation(x["citation_doi"], x["citation_pubmed"]), axis = 1)
df = df.drop(columns=["citation_doi", "citation_pubmed"])
df.to_csv(f"{output_folder}/all_data.csv", index=False)
