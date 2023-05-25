import requests
from bs4 import BeautifulSoup
from os import makedirs

raw_folder = "../../raw_data/peptidedb/"
makedirs(raw_folder, exist_ok=True)

families = ["Cytokines and growth factor", "Peptide Hormones", "Antimicrobial peptides", "Toxins and venom peptides", "Antifreeze", "Other families", "Unique peptides"]
for family in families:
    url = f"http://www.peptides.be/index.php?p=pepfasta&accession_number=&name=&organism_group=&organism_species=&length_from=&length_to=&mass_from=&mass_to=&family_group={family}&family=&uniprot=&aminoacid=&submitbutton=Submit&breakout=1&context=search"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="lxml")
    sequences = soup.text
    with open(f"../../raw_data/peptidedb/{family}.txt", "w", encoding="utf-8") as file:
        file.write(sequences)
