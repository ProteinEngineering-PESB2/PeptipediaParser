from selenium import webdriver
from selenium.webdriver.common.by import By
from os import makedirs
from os.path import abspath
import time
raw_folder = abspath("../../raw_data/deep_afppred/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://abppred.anvil.app/")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "fa-cloud-download").click()
driver.find_elements(By.CLASS_NAME, "anvil-inlinable")[8].click()
driver.find_elements(By.CLASS_NAME, "anvil-inlinable")[9].click()