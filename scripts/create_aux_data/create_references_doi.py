import metapub as metapub
import pandas as pd
import tqdm
import requests

aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"


class CrossRefClient(object):
 
	def __init__(self, accept='text/x-bibliography; style=apa', timeout=3):
		"""
		# Defaults to APA biblio style
		
		# Usage:
		s = CrossRefClient()
		print s.doi2apa("10.1038/nature10414")		
		"""
		self.headers = {'accept': accept}
		self.timeout = timeout
 
	def query(self, doi, q={}):
		if doi.startswith("http://"):
			url = doi
		else:
			url = "http://dx.doi.org/" + doi
		
		r = requests.get(url, headers = self.headers)
		return r

	def doi2apa(self, doi):
		self.headers['accept'] = 'text/x-bibliography; style=apa'
		return self.query(doi).text

df = pd.read_csv(f"{output_folder}/all_data.csv")
ids = df[["doi"]].dropna()
ids = ids.astype(str)
ids = ids.drop_duplicates()
for index, row in tqdm.tqdm(ids.iterrows()):
	s = CrossRefClient()
	ids.loc[index, "citation_doi"] = s.doi2apa(row.doi)
ids.to_csv(f"{aux_data_folder}/dois.csv", index=False)
exit()
df = df.merge(ids, on="doi", how="left")
print(df)

def combine_citation(doi, pubmed):
	
	if pubmed is not None:
		text = pubmed
	elif doi is not None:
		text = doi
	return text.replace('""', '')

df["citation"] = df.apply(lambda x: combine_citation(x["citation_doi"], x["citation_pubmed"]), axis = 1)
df = df.drop(columns=["citation_doi", "citation_pubmed"])
df.to_csv(f"{output_folder}/all_data.csv", index=False)
