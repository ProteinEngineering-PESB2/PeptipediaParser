import pandas as pd
import shutil
shutil.copy("../../auxiliar_data/pfam.csv", "../../tables/pfam.csv") #tabla tal cual
phgo = pd.read_csv("../../auxiliar_data/php.csv")
peptides = pd.read_csv("../../tables/peptide.csv")
phgo = phgo.merge(peptides, on="sequence", how="left")
phgo = phgo[["id_peptide", "id_pfam"]]
phgo = phgo.dropna()
phgo = phgo.drop_duplicates()
phgo = phgo.rename(columns={"id_sequence":"id_peptide"})
phgo.to_csv("../../tables/peptide_has_pfam.csv", index=False) #peptide has pfam
