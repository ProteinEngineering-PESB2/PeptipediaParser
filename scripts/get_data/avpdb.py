from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from os import makedirs
from os.path import abspath
import os
raw_folder = abspath("../../raw_data/avpdb/")
makedirs(raw_folder, exist_ok=True)
url = "http://crdd.osdd.net/servers/avpdb/dd.php"

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get(url)
driver.find_elements(By.NAME, "DOWNLOAD")[0].click()
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    new_path = path.replace("(1)", "")
    os.rename(path, new_path)