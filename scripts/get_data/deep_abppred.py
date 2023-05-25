from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from os import makedirs
from os.path import abspath
import time
raw_folder = abspath("../../raw_data/deep_afppred/")
makedirs(raw_folder, exist_ok=True)

options = Options()
options.add_argument("-headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", raw_folder)
driver = webdriver.Firefox(options=options)

driver.get("https://abppred.anvil.app/")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "fa-cloud-download").click()
driver.find_elements(By.CLASS_NAME, "anvil-inlinable")[8].click()
driver.find_elements(By.CLASS_NAME, "anvil-inlinable")[9].click()