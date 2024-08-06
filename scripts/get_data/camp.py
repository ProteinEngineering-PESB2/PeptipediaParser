from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from os import makedirs
from os.path import abspath

raw_folder = abspath("../../raw_data/camp/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("http://www.camp3.bicnirrh.res.in/dbSearch/seqSearch.php")
driver.find_element(By.ID, "textbox1").send_keys("a")
select = Select(driver.find_element(By.ID, "dbFeature1"))
select.select_by_value("act")

driver.find_element(By.ID, "searchButton").click()
time.sleep(20)
table = driver.find_element(By.ID, "myForm").find_element(By.TAG_NAME, "table")
first_column = table.find_element(By.TAG_NAME, "tr")
inputs = first_column.find_elements(By.TAG_NAME, "input")
inputs[0].click()
inputs[2].click()
