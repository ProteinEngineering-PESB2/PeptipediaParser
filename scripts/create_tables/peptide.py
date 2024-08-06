"""Creates peptide table"""
import pandas as pd
import datetime as datetime

df = pd.read_csv("../../output/all_data.csv")
reference = df.copy()[["id_sequence", "citation"]].drop_duplicates().dropna(subset="citation")
reference = reference.groupby("id_sequence")["citation"].apply(lambda x: '\n'.join(x))

patent = df.copy()[["id_sequence", "patent"]].drop_duplicates().dropna(subset="patent")
patent = patent.groupby("id_sequence")["patent"].apply(lambda x: '|'.join(x))

keyword = df.copy()[["id_sequence", "keyword"]].drop_duplicates().dropna(subset="keyword")
keyword = keyword.groupby("id_sequence")["keyword"].apply(lambda x: ', '.join(x))

half_life = df[["sequence", "half_life"]].copy().dropna()
half_life = half_life.groupby("sequence", as_index=False)["half_life"].apply(lambda x: ", ".join(x))

df = df[["id_sequence", "sequence", "is_canon", "nutraceutical", "swissprot_id"]]
df = df.drop_duplicates()

phy = pd.read_csv("../../auxiliar_data/physicochemical.csv") #Gets physicochemical data from table
peptides = df.merge(phy, on="sequence", how="left")
peptides["act_date"] = datetime.date.today()

peptides = peptides.merge(reference, on="id_sequence", how="left")
peptides = peptides.merge(patent, on="id_sequence", how="left")
peptides = peptides.merge(keyword, on="id_sequence", how="left")
peptides = peptides.rename(columns={"id_sequence": "id_peptide", "citation": "reference"})
peptides = peptides.merge(half_life, on="sequence", how="left")
print(peptides)
peptides.to_csv("../../tables/peptide.csv", index=False) #Create peptide table
