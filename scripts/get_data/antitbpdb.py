import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import makedirs
datas = []
i = 1
while True: #14 pages now
    res = requests.get(f"https://webs.iiitd.edu.in/raghava/antitbpdb/browse_sub1.php?token=Linear&col=8&page={i}")
    soup = BeautifulSoup(res.text, features='lxml')
    a  = soup.find("table").prettify()
    df = pd.read_html(a)[0]
    datas.append(df)
    last_pagination = soup.find("div", {"class": "pagination"}).find_all("a")[-1].text.strip()
    if last_pagination != "next":
        break
    else:
        i+=1
df = pd.concat(datas)
raw_folder = "../../raw_data/antitbpdb/"
makedirs(raw_folder, exist_ok=True)
df.to_csv(f"{raw_folder}/data.csv", index=False)