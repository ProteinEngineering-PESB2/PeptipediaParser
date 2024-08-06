"""AllergenOnline"""
import pandas as pd
import os
from utils import verify_sequences, raw_folder, parsed_folder
from Bio import SeqIO

try:
    pdb_path = f"{raw_folder}/rcsb_pdb/pdb_seqres.txt"
    compare_path = f"{raw_folder}/compare/COMPARE-2023-FastA-Seq.txt"
    raw_folder = f"{raw_folder}/allergenonline/"
    filename = "Browse the Database.csv"
    compare = pd.DataFrame([[a.id.split()[0], str(a.seq)]
                            for a in list(SeqIO.parse(compare_path, "fasta"))],
                            columns=["id", "sequence"])
    pdb = pd.DataFrame([[a.id.split()[0].upper(), str(a.seq)]
                        for a in list(SeqIO.parse(pdb_path, "fasta"))],
                        columns=["id", "sequence"])
    path = os.path.join(raw_folder, filename)
    data = pd.read_csv(path, sep=",")
    merged = data.merge(compare, left_on="Accession", right_on="id")
    merged2 = data.merge(pdb, left_on="Accession", right_on="id")
    merged = pd.concat([merged, merged2])
    rest_ids = pd.Series([str(a).split(".", maxsplit=1)[0]
                          for a in list(set(data.Accession) - set(merged.Accession))
                          if a is not None])
    rest = pd.DataFrame()
    rest["id"] = rest_ids
    rest_merged = compare.merge(rest, right_on="id", left_on="id")
    data = pd.concat([merged, rest_merged])[["sequence"]]
    data["activity"] = "allergen"
    data["sequence"],data["is_canon"] = zip(*data["sequence"].map(verify_sequences))
    data = data.dropna(subset=["sequence"])
    data = data.drop_duplicates()
    data.to_csv(os.path.join(f"{parsed_folder}/allergenonline.csv"), index=False)

    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)