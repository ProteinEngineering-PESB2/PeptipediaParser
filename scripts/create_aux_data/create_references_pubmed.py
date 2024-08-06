import metapub as metapub
import pandas as pd
import eutils
import tqdm
import requests

aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"

pubmed_ids = pd.read_csv(f"{aux_data_folder}/pubmeds.csv")
pubmed_ids.citation_pubmed = pubmed_ids.citation_pubmed.fillna("")
for index, row in tqdm.tqdm(pubmed_ids.iterrows()):
    if row.citation_pubmed == "":
        try:
            fetcher = metapub.PubMedFetcher()
            f = fetcher.article_by_pmid(row.pubmed)
            pubmed_ids.loc[index, "citation_pubmed"] = f.citation
        except metapub.exceptions.InvalidPMID as e:
            pass
        except eutils._internal.exceptions.EutilsNCBIError as e:
            pass
        except requests.exceptions.ConnectionError as e:
            pass
        except KeyboardInterrupt as k:
            raise KeyboardInterrupt
        except Exception as e:
            pass
    if index % 1000 == 0:
        pubmed_ids.to_csv(f"{aux_data_folder}/pubmeds.csv", index=False)
pubmed_ids.to_csv(f"{aux_data_folder}/pubmeds.csv", index=False)
