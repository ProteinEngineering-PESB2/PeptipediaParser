import requests
from bs4 import BeautifulSoup
import pandas as pd

import requests
class Uniprot:
    """Find sequence in uniprot files"""
    def __init__(self):
        self.uniprot_path = """https://rest.uniprot.org/uniprotkb/{}.fasta"""
    def get_sequence(self, uniprot_id):
        print(uniprot_id)
        try:
            response = requests.get(
                self.uniprot_path.format(uniprot_id), timeout=10000)
            if response.status_code == 200:
                sequence = "".join(response.text.splitlines()[1:])
                return sequence
        except:
            pass

bactibase = pd.read_csv("../../raw_data/bactibase/bactibase.csv")
swissprot = pd.read_csv("../../parsed_data/swissprot.csv")
merged = bactibase.merge(swissprot, left_on="UniProt", right_on="id")
merged["activity"] = '["bacteriocin", "antimicrobial", "antibacterial"]'
merged["activity"] = merged["activity"].map(eval)
merged = merged.explode("activity")
merged = merged[["sequence", "activity"]]
merged = merged.dropna()
merged = merged.drop_duplicates()
print(merged)
merged.to_csv("../../parsed_data/bactibase.csv", index=False)
