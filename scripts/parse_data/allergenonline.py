import pandas as pd
import os
from functions import verify_sequences
from Bio import SeqIO
raw_folder = "../../raw_data/allergenonline/"
filename = "Browse the Database.csv"
compare_path = "../../raw_data/compare/COMPARE-2023-FastA-Seq.txt"
compare = pd.DataFrame([[a.id.split()[0], str(a.seq)] for a in list(SeqIO.parse(compare_path, "fasta"))], columns=["id", "sequence"])
pdb_path = "../../raw_data/rcsb_pdb/pdb_seqres.txt"
pdb = pd.DataFrame([[a.id.split()[0].upper(), str(a.seq)] for a in list(SeqIO.parse(pdb_path, "fasta"))], columns=["id", "sequence"])
path = os.path.join(raw_folder, filename)
data = pd.read_csv(path, sep=",")
merged = data.merge(compare, left_on="Accession", right_on="id")
merged2 = data.merge(pdb, left_on="Accession", right_on="id")
merged = pd.concat([merged, merged2])
rest_ids = pd.Series([str(a).split(".")[0] for a in list(set(data.Accession) - set(merged.Accession)) if a != None])
rest = pd.DataFrame()
rest["id"] = rest_ids
rest_merged = compare.merge(rest, right_on="id", left_on="id")
data = pd.concat([merged, rest_merged])[["sequence"]]
data["activity"] = "allergen"
data["sequence"] = data["sequence"].map(verify_sequences)
data = data.dropna(subset=["sequence"])
data = data.drop_duplicates()
print(data)
data.to_csv(os.path.join("../../parsed_data/allergenonline.csv"), index=False)
