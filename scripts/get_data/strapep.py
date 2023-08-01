#http://isyslab.info/StraPep/browse.php?classification=Antimicrobial
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from os import makedirs
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

raw_folder = "../../raw_data/strapep/"
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

dfs = []
activities = ["Antimicrobial", "Toxin and venom peptide", "Cytokine/Growth factor", "Hormone", "Neuropeptide", "Other"]
for act in activities:
    driver.get(f"http://isyslab.info/StraPep/browse.php?classification={act}")
    while(True):
        select = Select(driver.find_element(By.NAME, "browse_table_length"))
        select.select_by_value('100')
        data = driver.find_element(By.TAG_NAME, "table").get_attribute("outerHTML")
        data = pd.read_html(data)[0]
        dfs.append(data)
        next = driver.find_element(By.ID, "browse_table_next")
        if "disabled" in next.get_attribute("class"):
            break
        next.click()
df = pd.concat(dfs)
df.to_csv(f"{raw_folder}/data.csv", index=False)