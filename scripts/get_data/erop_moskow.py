import requests
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import tqdm
raw_folder = "../../raw_data/erop_moscow/"
"""makedirs(raw_folder, exist_ok=True)
res = requests.get("http://erop.inbi.ras.ru/query-erop.php?submit=%C2%A0%C2%A0Query+EROP%C2%A0%C2%A0%C2%A0")
soup = BeautifulSoup(res.text, features="lxml")
select = soup.find("select", {"name":"FUNC_CL__K"})
activities = [i["value"] for i in select.find_all("option") if i["value"] != ""]
urls = [f"http://erop.inbi.ras.ru/result1.php?EROP_NMB_K=&PEP_NAME_K=&FAM_NAME_K=&ALL_KAR__K=&ALL_KGD__K=&ALL_PHYL_K=&ALL_B_CL_K=&Organism=&SPECIES__K=&ALL_TISS_K=&SEQ_1____K=&AAR_SUM__K1=&AAR_SUM__K2=&M_W______K1=&M_W______K2=&PI_______K1=&PI_______K2=&POSIT_CH_K1=&POSIT_CH_K2=&NEGAT_CH_K1=&NEGAT_CH_K2=&NET_CH___K1=&NET_CH___K2=&FUNC_CL__K={activity}&FUNCTION_K=&SEQ_REFA_V=&SEQ_REFT_V=&SEQ_REFJ_V=&YEAR_SEQ_V1=&YEAR_SEQ_V2=&COUNTRY__V=&page_mode=View_Fasta" for activity in activities]
names = [f"{a}.fasta" for a in activities]
for url, filename in zip(urls, names):
    try:
        path = join(raw_folder, filename)
        with open(path, encoding="utf-8", mode="w") as file:
            soup = BeautifulSoup(requests.get(url).text, features="lxml").find("p")
            a = soup.prettify().split("\n")
            a = "\n".join([i.strip() for i in a if i.strip() != "<br/>"]).replace("</p>", "").replace("<p>", "").replace("&gt;", ">")
            file.write(a)
    except:
        print("Error:", filename)
"""
import os
import pandas as pd
from Bio import SeqIO
from metapub import PubMedFetcher
from multiprocessing import Pool
import time
def get_info(id):
    try:
        url = f"http://erop.inbi.ras.ru/result2.php?PepName={id}&SubSeq="
        soup = requests.get(url).text
        inicio = soup.find("Title:")
        fin = inicio + 200
        title = soup[inicio + 10:fin]
        title = title.split("</font>")[0].strip()
        return [id, title]
    except:
        return [None, None]

if __name__ == "__main__":
    fetch = PubMedFetcher()

    raw_folder = f"{raw_folder}"
    dfs = []
    #files = ["potentiator.fasta", "antiinflammatory.fasta", "taste.fasta",
    #         "stimulator.fasta", "synthesis stimulator.fasta"]
    files = os.listdir(raw_folder)
    for file in files:

        if ".fasta" in file:
            path = os.path.join(raw_folder, file)
            title = pd.DataFrame([[str(a.id).split("|")[0], str(a.seq)] for a in list(SeqIO.parse(path, "fasta"))], columns=["id", "sequence"])
            dfs.append(title)
    df = pd.concat(dfs)
    df = df.dropna()
    print(df)
    ids = df["id"].tolist()

    inicio = time.time()
    with Pool(100) as p:
        df = p.map(get_info, ids)
    fin = time.time()
    df = pd.DataFrame(df, columns=["id", "title"])
    df = df.dropna()
    print(df)
    print("títulos obtenidos")

    titles = df[["title"]].copy().drop_duplicates()
    print(titles)
    for index, row in tqdm.tqdm(titles.iterrows()):
        if row.title is not None:
            try:
                pmids = fetch.pmids_for_query(row.title, retmax=1)
                titles.loc[index, "pubmed"] = str(pmids)
            except Exception as e:
                print(row.title, e)
    df = df.merge(titles, on="title", how="left")[["id", "pubmed"]]
    print(df)
    df.to_csv("../../raw_data/erop_moscow/references.csv", index=False)
