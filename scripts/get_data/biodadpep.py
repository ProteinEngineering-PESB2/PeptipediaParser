#https://omicsbase.com/BioDADPep/biodadpep-search/
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from os import makedirs

raw_folder = "../../raw_data/biodadpep"
makedirs(raw_folder)
url = "https://omicsbase.com/BioDADPep/biodadpep-search/"

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get(url)
datas = []
a = driver.find_elements(By.ID, "table_1_wrapper")
while a == []:
    time.sleep(2)
    a = driver.find_elements(By.ID, "table_1_wrapper")
class_button = ""
while "disabled" not in class_button: #255 pages
    time.sleep(2)
    data = pd.read_html(a[0].get_attribute('innerHTML'))[0]
    datas.append(data)
    button = driver.find_element(By.ID, "table_1_next")
    class_button = button.get_attribute("class")
    button.click()
driver.quit()
df = pd.concat(datas)
df.to_csv(f"{raw_folder}/biodadpep.csv", index=False)
