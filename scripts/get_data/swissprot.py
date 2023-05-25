from os import makedirs
import wget
import gzip
raw_data = "../../raw_data/swissprot/"
makedirs(raw_data, exist_ok=True)
file = wget.download(
    "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz",
    f"{raw_data}uniprot_sprot.fasta.gz")

with gzip.open(file, 'rb') as f:
    file_content = f.read().decode(encoding="utf-8")
    with open(f"{raw_data}/uniprot_sprot.fasta", mode="w", encoding="utf-8") as output_fasta:
        output_fasta.write(file_content)