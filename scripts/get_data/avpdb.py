from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from os import makedirs
from os.path import abspath
import os
raw_folder = abspath("../../raw_data/avpdb/")
makedirs(raw_folder, exist_ok=True)
url = "http://crdd.osdd.net/servers/avpdb/dd.php"
options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", raw_folder)
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
driver.get(url)
driver.find_elements(By.NAME, "DOWNLOAD")[0].click()
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    new_path = path.replace("(1)", "")
    os.rename(path, new_path)