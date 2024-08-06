#http://split4.pmfst.hr/dadp/?a=list
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import makedirs
from os.path import abspath
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


raw_folder = abspath("../../raw_data/dadp/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("http://split4.pmfst.hr/dadp/?a=list")

try:
    element_present = EC.text_to_be_present_in_element((By.TAG_NAME, "table"), "/")
    WebDriverWait(driver, 100).until(element_present)

except TimeoutException:
    print("No encontrado")

table = driver.find_element(By.TAG_NAME, "table").get_attribute('innerHTML')
table = pd.read_html(table)[0]

table.to_csv(raw_folder+"/dadp.csv", index=False)