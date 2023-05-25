from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd
from os import makedirs
import time
from os.path import abspath
url = "http://crdd.osdd.net/servers/hipdb/dd.php"

raw_folder = abspath("../../raw_data/hipdb/")
makedirs(raw_folder, exist_ok=True)

options = Options()
options.add_argument("-headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", raw_folder)
driver = webdriver.Firefox(options=options)

driver.get(url)
driver.find_elements(By.NAME, "DOWNLOAD")[1].click()