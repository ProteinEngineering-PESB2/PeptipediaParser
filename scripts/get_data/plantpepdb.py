from os import makedirs
from os.path import abspath
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
raw_folder = abspath("../../raw_data/plantpepdb/")
makedirs(raw_folder, exist_ok=True)

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)


main_url = "http://14.139.61.8/PlantPepDB/pages/bro.php#18"
driver.get(main_url)
links = driver.find_elements(By.TAG_NAME, "ul")[-1].find_elements(By.TAG_NAME, "a")
count_links = len(links)
for i in range(count_links):
    url = links[i].get_attribute("href")
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(i+2))
    new_window = driver.window_handles[-1]
    original_window = driver.window_handles[0]
    driver.switch_to.window(new_window)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'feature-content')))
    driver.find_element(By.ID, "feature-content").find_element(By.TAG_NAME, "a").click()
    driver.get(main_url)
    links = driver.find_elements(By.TAG_NAME, "ul")[-1].find_elements(By.TAG_NAME, "a")
driver.close()
df = pd.concat([pd.read_csv(os.path.join(raw_folder, file), sep="\t") for file in os.listdir(raw_folder)])
def get_sequence(id):
    try:
        url = f"http://14.139.61.8/PlantPepDB/pages/information.php?id={id}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, features="lxml")
        sequence = soup.find("table").find_all("tr")[12].find_all("td")[-1].text
        return sequence
    except:
        print("Error:", i )
        pass
df["sequence"] = df["PPepDB-ID"].map(get_sequence)
df = df.dropna(subset="sequence")
df.to_csv("../../raw_data/plantpepdb.csv", index=False)