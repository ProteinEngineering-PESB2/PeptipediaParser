#http://dramp.cpu-bioinfor.org/downloads/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from os import makedirs
from os.path import abspath
from generic_getter import getter
raw_folder = abspath("../../raw_data/dramp/")
makedirs(raw_folder, exist_ok=True)

options = Options()
options.add_argument("-headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", raw_folder)
driver = webdriver.Firefox(options=options)
url = "http://dramp.cpu-bioinfor.org/downloads/"
driver.get(url)
a = driver.find_elements(By.TAG_NAME, "table")[1].find_elements(By.TAG_NAME, "a")
a = [i for i in a if ".fasta" in i.get_attribute("href")]
for i in a:
    i.click()