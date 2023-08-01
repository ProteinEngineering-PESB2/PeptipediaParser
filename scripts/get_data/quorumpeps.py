from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from os import makedirs
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
raw_folder = "../../raw_data/quorumpeps/"
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://quorumpeps.ugent.be/search")
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, "table")))
table = driver.find_element(By.ID, "table")
table = pd.read_html(table.get_attribute("outerHTML"))[0]
table.to_csv(f"{raw_folder}/quorumpeps.csv", index=False)