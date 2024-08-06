from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from os import makedirs
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
raw_folder = "../../raw_data/quorumpeps/"
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
#chromeOptions.add_argument("--headless")
#chromeOptions.add_argument('--ignore-ssl-errors=yes')
#chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://quorumpeps.ugent.be/")
form = driver.find_element(By.TAG_NAME, "form")
button = form.find_element(By.TAG_NAME, "button")
button.click()
WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located((By.ID, "table")))
links = driver.find_element(By.ID, "table").find_elements(By.TAG_NAME, "a").copy()
links = [ia for ia, a in enumerate(links) if "publication" in a.get_attribute("href")]
print(links)

exit()
for i_link, link in enumerate(links):
    href = links[i_link].get_attribute("href")
    if "publication" in href:
        link.click()
        WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, "Download")))
        pubmed = driver.find_element(By.LINK_TEXT, "Download")
        print(pubmed.get_attribute("href"))
        driver.execute_script("window.history.go(-1)")
        time.sleep(10)
        links = driver.find_element(By.ID, "table").find_elements(By.TAG_NAME, "a")

table_html = driver.find_element(By.ID, "table").get_attribute("outerHTML")
#print(table_html)
table = pd.read_html(table_html)[0]
table.to_csv(f"{raw_folder}/quorumpeps.csv", index=False)