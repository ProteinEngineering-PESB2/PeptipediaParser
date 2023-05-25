from os import makedirs
from os.path import abspath
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

raw_folder = abspath("../../raw_data/baamps/")
makedirs(raw_folder, exist_ok=True)

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", raw_folder)
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
driver.get("http://www.baamps.it/browse")
element = driver.find_element(By.ID, "queryExport")
driver.execute_script("arguments[0].click();", element)
