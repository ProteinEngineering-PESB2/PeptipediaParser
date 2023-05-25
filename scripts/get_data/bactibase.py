import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import makedirs
import requests
raw_folder = "../../raw_data/bactibase"
makedirs(raw_folder, exist_ok=True)
data = requests.get("http://bactibase.hammamilab.org/bacteriocinslist.php?RecPerPage=ALL")
data = BeautifulSoup(data.text, features="lxml")
data = pd.read_html(data.find("table").prettify())[0]
data.to_csv(f"{raw_folder}/bactibase.csv", index=False)