from generic_getter import getter
from os.path import abspath
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


raw_folder = abspath("../../raw_data/arachnoserver/")
urls = ["https://arachnoserver.qfab.org/fasta/all.pep.fa"]
getter(urls, raw_folder = "../../raw_data/arachnoserver/")


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : raw_folder}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--ignore-ssl-errors=yes')
chromeOptions.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://arachnoserver.qfab.org/advancedsearch.html")
advanced = driver.find_element(By.NAME, "advanced")
timeout = 200

select = Select(advanced.find_element(By.ID, "1.fields"))
select.select_by_value("2-mullist-activity.id-toxin.activities as activity")

try:
    element_present = EC.text_to_be_present_in_element((By.ID, "1.mullist.choices"), "Antiarrhythmic")
    WebDriverWait(advanced, timeout).until(element_present)

except TimeoutException:
    print("No encontrado")

select = Select(advanced.find_element(By.ID, "1.mullist.choices"))
select_options = [op.text for op in select.options]
len_options = len(select_options)
for i in range(len_options):
    select.select_by_visible_text(select_options[i])
    advanced.find_element(By.NAME, "search").click()

    try:
        element_present = EC.presence_of_element_located((By.NAME, "getFastas"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("No encontrado")
    time.sleep(1)

    select = Select(driver.find_element(By.NAME, "sequenceType"))
    select.select_by_visible_text("Peptide")

    driver.find_element(By.NAME, "getFastas").click()
    
    try:
        element_present = EC.presence_of_element_located((By.TAG_NAME, "pre"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("No encontrado")

    fasta_text = driver.find_element(By.TAG_NAME, "pre").text
    with open(raw_folder+"/"+select_options[i]+".fasta", mode="w", encoding="utf-8") as file:
        file.write(fasta_text)

    driver.get("https://arachnoserver.qfab.org/advancedsearch.html")
    advanced = driver.find_element(By.NAME, "advanced")
    timeout = 100

    select = Select(advanced.find_element(By.ID, "1.fields"))
    select.select_by_value("2-mullist-activity.id-toxin.activities as activity")

    try:
        element_present = EC.text_to_be_present_in_element((By.ID, "1.mullist.choices"), "Antiarrhythmic")
        WebDriverWait(advanced, timeout).until(element_present)

    except TimeoutException:
        print("No encontrado")

    select = Select(advanced.find_element(By.ID, "1.mullist.choices"))