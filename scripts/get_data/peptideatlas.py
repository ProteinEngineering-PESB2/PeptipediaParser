import requests
from bs4 import BeautifulSoup
from os import makedirs
from generic_getter import getter
raw_folder = "../../raw_data/peptideatlas/"
makedirs(raw_folder, exist_ok=True)
res = requests.get("https://peptideatlas.org/builds/")
soup = BeautifulSoup(res.text, features="lxml")
links = [f"https://peptideatlas.org/builds/{a['href']}" for a in soup.find_all("a") if ".fasta" in a.text]
getter(links, raw_folder)