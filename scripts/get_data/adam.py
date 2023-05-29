#https://bioinformatics.cs.ntou.edu.tw/adam/search_adam.php
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from os import makedirs
from os.path import abspath
import pandas as pd

raw_folder = abspath("../../raw_data/adam/")
makedirs(raw_folder, exist_ok=True)

options = Options()
options.add_argument("-headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", raw_folder)
driver = webdriver.Firefox(options=options)

driver.get("https://bioinformatics.cs.ntou.edu.tw/adam/search_adam.php")
table = driver.find_elements(By.TAG_NAME, "table")[1].get_attribute("outerHTML")
data = pd.read_html(table, header=1)[0]
data.to_csv(f"{raw_folder}/data.csv", index=False)