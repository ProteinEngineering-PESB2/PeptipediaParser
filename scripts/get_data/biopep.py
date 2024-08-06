import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import makedirs

raw_folder = "../../raw_data/biopep"
makedirs(raw_folder, exist_ok=True)

res = requests.get(f"https://biochemia.uwm.edu.pl/biopep/activity_dic_list.php")
soup = BeautifulSoup(res.text, features="lxml")
table = soup.find("table").prettify()
df = pd.read_html(table, header = 0)[0]
df = pd.DataFrame(zip(*df["Activity code | Description"].str.split("|"))).T
df = df[[1]]
df = df.rename(columns={1: "activity"})
df.activity = df.activity.str.strip()
data = []
for activity in df.activity: #56 now
    url = f"https://biochemia.uwm.edu.pl/biopep/peptide_data_search.php?txt_search={activity}&menu_search=activity&button12.x=14&button12.y=10"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="lxml")
    table = soup.find("table").prettify()
    peptides = pd.read_html(table, header=1)[0]
    data.append(peptides)
df = pd.concat(data)
df.to_csv(f"{raw_folder}/biopep.csv")