import requests
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs

raw_folder = "../../raw_data/erop_moskow/"
makedirs(raw_folder, exist_ok=True)
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