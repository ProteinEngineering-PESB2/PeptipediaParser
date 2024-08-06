from os import makedirs
import wget
import gzip
raw_data = "../../raw_data/conoserver/"
makedirs(raw_data, exist_ok=True)
file = wget.download(
    "http://www.conoserver.org/download/conoserver_protein.fa.gz",
    f"{raw_data}conoserver_protein.fa.gz")

with gzip.open(file, 'rb') as f:
    file_content = f.read().decode(encoding="utf-8")
    with open(f"{raw_data}/conoserver_protein.fa", mode="w", encoding="utf-8") as output_fasta:
        output_fasta.write(file_content)