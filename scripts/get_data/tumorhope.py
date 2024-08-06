import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import makedirs
raw_folder = "../../raw_data/tumorhope/"
makedirs(raw_folder, exist_ok=True)
res = requests.get("https://webs.iiitd.edu.in/raghava/tumorhope/searchtumor.php")
soup = BeautifulSoup(res.text, features="lxml")
a = soup.find("table")
table = pd.read_html(a.prettify())[0]
table.to_csv(f"{raw_folder}/tumorhope.csv", index=False)