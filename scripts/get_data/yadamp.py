import pandas as pd
from os import makedirs
from os.path import abspath
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
raw_folder = abspath("../../raw_data/yadamp/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get(main_url)
driver.find_element(By.TAG_NAME, "center").find_elements(By.TAG_NAME, "input")[0].click()
table = driver.find_element(By.TAG_NAME, "table")
df = pd.read_html(table.get_attribute("outerHTML"))[0]
df.to_csv(f"{raw_folder}/data.csv", index=False)