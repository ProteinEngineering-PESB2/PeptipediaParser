from os import makedirs
import wget
import gzip
raw_data = "../../raw_data/rcsb_pdb/"
makedirs(raw_data, exist_ok=True)
filename = "pdb_seqres.txt"
file = wget.download(
    "https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt.gz",
    f"{raw_data}/{filename}.gz")

with gzip.open(file, 'rb') as f:
    file_content = f.read().decode(encoding="utf-8")
    with open(f"{raw_data}/{filename}", mode="w", encoding="utf-8") as output_fasta:
        output_fasta.write(file_content)