import pandas as pd
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from os.path import abspath
from os import makedirs
from generic_getter import getter
import pandas as pd
peptides = []
raw_folder = abspath("../../raw_data/lamp2/")
makedirs(raw_folder, exist_ok=True)

getter(["http://biotechlab.fudan.edu.cn/database/lamp/db/lamp2.fasta"], raw_folder)
dfs = []
for type_amp in ["antiviral", "antibacterial", "antifungal", "antiparasitic", "antitumor"]:
    res = requests.get(f"http://biotechlab.fudan.edu.cn/database/lamp/browse.php?page=1&group={type_amp}")
    soup = BeautifulSoup(res.text, features="lxml")
    pages = int(soup.find("div", {"class": "page_nav"}).text.split(" pages")[0].split("Total ")[1])
    for i in range(1, pages+1):
        res = requests.get(f"http://biotechlab.fudan.edu.cn/database/lamp/browse.php?page={i}&group={type_amp}")
        soup = BeautifulSoup(res.text, features="lxml")
        content = soup.find_all("ul", {"class": "hlist"})
        a_s = []
        for con in content:
            a_s += con.find_all("a")
        for a in a_s:
            id_peptide = a["href"].split("id=")[1]
            peptides.append(id_peptide)
    df = pd.DataFrame()
    df["id"] = peptides
    df["activity"] = type_amp
    dfs.append(df)
df = pd.concat(dfs)
df.to_csv(raw_folder+"/lamp2_activities.csv", index=False)