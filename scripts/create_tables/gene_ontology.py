import pandas as pd
import shutil
shutil.copy("../../auxiliar_data/gene_ontology.csv", "../../tables/gene_ontology.csv") #Gene_onotlogy table
phgo = pd.read_csv("../../auxiliar_data/phgo.csv")
peptides = pd.read_csv("../../tables/peptide.csv")
phgo = phgo.merge(peptides, on="sequence", how="left")
phgo = phgo[["id_peptide", "id_go"]]
phgo = phgo.dropna()
phgo.to_csv("../../tables/peptide_has_go.csv", index=False) #Peptide has go table
