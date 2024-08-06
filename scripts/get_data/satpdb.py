#https://webs.iiitd.edu.in/raghava/satpdb/antibacterial.fasta
import requests
from bs4 import BeautifulSoup
from generic_getter import getter
res = requests.get("https://webs.iiitd.edu.in/raghava/satpdb/down.php")
soup = BeautifulSoup(res.text, features="lxml")
table = soup.find("table")
refs = table.find_all("a")
urls = [f"https://webs.iiitd.edu.in/{a['href']}" for a in refs]
getter(urls, "../../raw_data/satpdb/")