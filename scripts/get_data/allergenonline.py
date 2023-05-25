from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from os import makedirs
from os.path import abspath
raw_folder = abspath("../../raw_data/allergenonline/")
makedirs(raw_folder, exist_ok=True)

options = Options()
options.add_argument("-headless")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", raw_folder)
driver = webdriver.Firefox(options=options)

driver.get("http://www.allergenonline.org/databasebrowse.shtml")
driver.find_element(By.TAG_NAME, "main").find_elements(By.TAG_NAME, "button")[1].click()