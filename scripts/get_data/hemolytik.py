from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd
from os import makedirs
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

raw_folder = "../../raw_data/hemolytik/"
makedirs(raw_folder, exist_ok=True)

options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
for act in ["Antimicrobial", "Anticancer", "Antifungal", "Antibacterial", "toxi", "CPP", "Antiparasitic"]:
    url = f"https://webs.iiitd.edu.in/raghava/hemolytik/browse_sub.php?token={act}&col=11"
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.current_url != url)
    dfs = []
    while True:
        try:
            myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'example')))
            table = driver.find_element(By.ID, "example").get_attribute("outerHTML")
            dfs.append( pd.read_html(table)[0])
        except:
            break
        try:
            myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'example_next')))
            next = driver.find_element(By.ID, "example_next")
            if "disabled" in next.get_attribute("class"):
                break
            next.click()
        except:
            break
    df = pd.concat(dfs)
    df.to_csv(f"{raw_folder}/{act}.csv", index=False)