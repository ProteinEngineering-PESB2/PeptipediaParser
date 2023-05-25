import pandas as pd
import requests
from bs4 import BeautifulSoup
data = pd.read_csv("../../raw_data/biopep/biopep.csv")
data = data[["1", "3"]]
data = data.rename(columns={"1": "id", "3": "sequence"})
data = data.sort_values(by="id")
for index, row in data.iterrows():
    try:
        url = f"https://biochemia.uwm.edu.pl/biopep/peptide_data_page1.php?zm_ID={row.id}"
        res = requests.get(url)
        a = BeautifulSoup(res.text, features="lxml")
        options = a.find_all("option")[2:]
        activity = [option.text.split()[0] for option in options if option.get("selected") == ""][0]
        data.loc[index, "activity"] = activity
    except:
        print("Error:", index)
data = data[["sequence", "activity"]]
data = data.drop_duplicates()
data.to_csv("../../parsed_data/biopep.csv", index=False)
print(data)