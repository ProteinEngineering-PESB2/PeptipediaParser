from generic_getter import getter
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import makedirs
from os.path import abspath
import tarfile
raw_folder = abspath("../../raw_data/dbamp/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

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