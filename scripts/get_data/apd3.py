from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from os import makedirs
raw_folder = "../../raw_data/apd3/"
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://aps.unmc.edu/database")


inputs = driver.find_element(By.TAG_NAME, "table").find_elements(By.TAG_NAME, "tr")[11].find_elements(By.TAG_NAME, "td")[-1]
labels  = [x.split(">")[1].strip() for x in inputs.get_attribute('innerHTML').split("<")[1:-1]]
labels = [x for x in labels if x != ""]
for input_num in range(len(labels)): #27 activities
    inputs = driver.find_element(By.TAG_NAME, "table").find_elements(By.TAG_NAME, "tr")[11].find_elements(By.TAG_NAME, "td")[-1].find_elements(By.TAG_NAME, "input")
    reset_form = driver.find_element(By.TAG_NAME, "table").find_elements(By.TAG_NAME, "tr")[-1].find_elements(By.TAG_NAME, "input")[-1]
    search_form = driver.find_element(By.TAG_NAME, "table").find_elements(By.TAG_NAME, "tr")[-1].find_elements(By.TAG_NAME, "input")[0]
    reset_form.click()
    inputs[input_num].click()
    search_form.click()
    table = driver.find_elements(By.ID, "selectID")[0].find_element(By.TAG_NAME, "table")
    table = pd.read_html(table.get_attribute("outerHTML"))[0]
    table.to_csv(f"{raw_folder}/{labels[input_num].replace('/', '_')}.csv", index=False)
    driver.back()