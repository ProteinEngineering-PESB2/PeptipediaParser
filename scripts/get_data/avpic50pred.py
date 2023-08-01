from selenium import webdriver
from selenium.webdriver.common.by import By
from os import makedirs
from os.path import abspath
import time
raw_folder = abspath("../../raw_data/avpic50pred/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("http://crdd.osdd.net/servers/ic50avp/datasets.php")
time.sleep(2)
links = driver.find_element(By.TAG_NAME, "center")
links = links.find_elements(By.NAME, "DOWNLOAD")
for link in links:
    link.click()