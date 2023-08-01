import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from os import makedirs
raw_folder = "../../raw_data/brainpeps/"
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://brainpeps.ugent.be/search")
time.sleep(10)
data = pd.read_html(driver.find_element(By.ID, "table").get_attribute("outerHTML"))[0]
data.to_csv(f"{raw_folder}/brainpeps.csv", index=False)