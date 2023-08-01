#https://bioinformatics.cs.ntou.edu.tw/adam/search_adam.php
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import makedirs
from os.path import abspath
import pandas as pd

raw_folder = abspath("../../raw_data/adam/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://bioinformatics.cs.ntou.edu.tw/adam/search_adam.php")
table = driver.find_elements(By.TAG_NAME, "table")[1].get_attribute("outerHTML")
data = pd.read_html(table, header=1)[0]
data.to_csv(f"{raw_folder}/data.csv", index=False)