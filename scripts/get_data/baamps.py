from os import makedirs
from os.path import abspath
from selenium import webdriver
from selenium.webdriver.common.by import By

raw_folder = abspath("../../raw_data/baamps/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)


driver.get("http://www.baamps.it/browse")
element = driver.find_element(By.ID, "queryExport")
driver.execute_script("arguments[0].click();", element)
