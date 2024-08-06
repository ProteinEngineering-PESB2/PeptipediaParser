from selenium import webdriver
from selenium.webdriver.common.by import By
from os import makedirs
from os.path import abspath
raw_folder = abspath("../../raw_data/celiac_database/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("http://www.allergenonline.org/celiacbrowse.shtml")
driver.find_element(By.TAG_NAME, "main").find_elements(By.TAG_NAME, "button")[1].click()