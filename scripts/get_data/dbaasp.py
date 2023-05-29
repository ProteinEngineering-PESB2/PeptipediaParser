from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from os import makedirs
from os.path import abspath
from os import rename
import time
raw_folder = abspath("../../raw_data/dbaasp/")
makedirs(raw_folder, exist_ok=True)

targets = ["Virus", "Biofilm", "Cancer", "Fungus", "Gram-", "Gram+", "Insect", "Mammalian Cell", "Mollicute", "Nematode", "Parasite", "Protista"]
for target in targets:
    url = f"https://dbaasp.org/search?id.value=&name.value=&sequence.value=&sequence.option=full&sequenceLength.value=&complexity.value=&synthesisType.value=&uniprot.value=&nTerminus.value=&cTerminus.value=&unusualAminoAcid.value=&intraChainBond.value=&interChainBond.value=&coordinationBond.value=&pubchem.value=&pubchemId.value=&threeDStructure.value=&kingdom.value=&source.value=&targetGroup.value={target}&synergy.value=&articleAuthor.value=&articleJournal.value=&articleYear.value=&articleVolume.value=&articlePages.value=&articleTitle.value="
    options = Options()
    options.add_argument("-headless")
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", raw_folder)
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    driver.find_element(By.CLASS_NAME, "export-fasta-data").click()
    time.sleep(10)
    rename(f"{raw_folder}/peptides-fasta.txt", f"{raw_folder}/{target}.fasta")