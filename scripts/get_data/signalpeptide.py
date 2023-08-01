#http://signalpeptide.de/?m=searchspdb
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from os import makedirs
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

raw_folder = "../../raw_data/signalpeptide/"
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("http://signalpeptide.de/?m=searchspdb")
form = driver.find_element(By.TAG_NAME, "form")
row = form.find_elements(By.TAG_NAME, "tr")[8]
select = Select(row.find_element(By.TAG_NAME, "select"))
select.select_by_value("confirmed")
form.find_elements(By.TAG_NAME, "tr")[-1].find_element(By.TAG_NAME, "input").click()
time.sleep(3)
table = driver.find_element(By.TAG_NAME, "table").get_attribute("outerHTML")
table = pd.read_html(table)[0]
print(table)
table.to_csv(raw_folder+"/signalpeptide.csv", index=False)