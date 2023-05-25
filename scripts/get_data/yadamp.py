import pandas as pd
from os import makedirs
from os.path import abspath
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
raw_folder = abspath("../../raw_data/yadamp/")
makedirs(raw_folder, exist_ok=True)
options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
main_url = "http://yadamp.unisa.it/searchDatabase.aspx"
driver.get(main_url)
driver.find_element(By.TAG_NAME, "center").find_elements(By.TAG_NAME, "input")[0].click()
table = driver.find_element(By.TAG_NAME, "table")
df = pd.read_html(table.get_attribute("outerHTML"))[0]
df.to_csv(f"{raw_folder}/data.csv", index=False)