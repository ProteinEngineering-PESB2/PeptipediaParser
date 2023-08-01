#http://dramp.cpu-bioinfor.org/downloads/
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import makedirs
from os.path import abspath
from generic_getter import getter
raw_folder = abspath("../../raw_data/dramp/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

url = "http://dramp.cpu-bioinfor.org/downloads/"
driver.get(url)
a = driver.find_elements(By.TAG_NAME, "table")[1].find_elements(By.TAG_NAME, "a")
a = [i for i in a if ".fasta" in i.get_attribute("href")]
for i in a:
    i.click()