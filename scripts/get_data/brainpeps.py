import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from os import makedirs
raw_folder = "../../raw_data/brainpeps/"
makedirs(raw_folder, exist_ok=True)

options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
driver.get("https://brainpeps.ugent.be/search")
time.sleep(10)
data = pd.read_html(driver.find_element(By.ID, "table").get_attribute("outerHTML"))[0]
data.to_csv(f"{raw_folder}/brainpeps.csv", index=False)