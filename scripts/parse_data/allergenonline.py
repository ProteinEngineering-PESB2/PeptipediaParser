import pandas as pd
from Bio import SeqIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
options = Options()
options.headless = True

compare_df = [[str(record.id), str(record.seq)] for record in SeqIO.parse("../../raw_data/compare/COMPARE-2023-FastA-Seq.txt", "fasta")]
compare_df = pd.DataFrame(compare_df, columns=["id", "sequence"])

allergen_sequences = []

driver = webdriver.Firefox(options=options)
a = pd.read_csv("../../raw_data/allergenonline/Browse the Database.csv")
for row in a["Accession"]:
    match = compare_df[compare_df.id == row]
    if len(match) != 0:
        allergen_sequences.append(str(match.sequence.values[0]))
    else:
        url = f"https://www.ncbi.nlm.nih.gov/protein/{row}?report=fasta"
        driver.get(url)
        time.sleep(2)
        try:
            a = driver.find_elements(By.ID, "viewercontent1")[0]
            sequence = "".join(a.text.splitlines()[1:])
            allergen_sequences.append(sequence)
        except Exception as e:
            print(e, row)
driver.quit()
allergenonline = pd.DataFrame()
allergenonline["sequence"] = allergen_sequences
allergenonline["activity"] = "allergen"

allergenonline = allergenonline[allergenonline.sequence.str.len() <= 150]
allergenonline.to_csv(".././parsed_data/allergenonline.csv", index=False)