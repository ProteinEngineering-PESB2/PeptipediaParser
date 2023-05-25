from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from os import makedirs
from os.path import abspath
import time
raw_folder = abspath("../../raw_data/avpic50pred/")
makedirs(raw_folder, exist_ok=True)

options = Options()
options.add_argument("-headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", raw_folder)
driver = webdriver.Firefox(options=options)

driver.get("http://crdd.osdd.net/servers/ic50avp/datasets.php")
time.sleep(2)
links = driver.find_element(By.TAG_NAME, "center")
links = links.find_elements(By.NAME, "DOWNLOAD")
for link in links:
    link.click()