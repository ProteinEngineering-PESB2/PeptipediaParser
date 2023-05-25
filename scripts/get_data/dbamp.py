from generic_getter import getter
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from os import makedirs
from os.path import abspath
import tarfile
raw_folder = abspath("../../raw_data/dbamp/")
makedirs(raw_folder, exist_ok=True)

options = Options()
options.add_argument("-headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", raw_folder)
driver = webdriver.Firefox(options=options)

driver.get("http://csb.cse.yzu.edu.tw/dbAMP/download.php")
a = driver.find_elements(By.TAG_NAME, "table")[1].find_elements(By.TAG_NAME, "a")
urls = [link.get_attribute("href") for link in a]
getter(urls, raw_folder)
driver.close()
for file in os.listdir(raw_folder):
    path = os.path.join(raw_folder, file)
    tar = tarfile.open(path)
    tar.extractall(raw_folder)
    tar.close()