from os import makedirs
import wget
import gzip
import requests
raw_data = "../../raw_data/swissprot/"
makedirs(raw_data, exist_ok=True)
"""file = wget.download(
    "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz",
    f"{raw_data}uniprot_sprot.fasta.gz")

with gzip.open(file, 'rb') as f:
    file_content = f.read().decode(encoding="utf-8")
    with open(f"{raw_data}/uniprot_sprot.fasta", mode="w", encoding="utf-8") as output_fasta:
        output_fasta.write(file_content)
"""
url_full = "https://rest.uniprot.org/uniprotkb/stream?fields=accession%2Creviewed%2Clit_pubmed_id%2Csequence&format=tsv&query=%28%28length%3A%5B2+TO+150%5D%29+AND+%28reviewed%3Atrue%29%29"
url_peptides = "https://rest.uniprot.org/uniprotkb/stream?fields=accession%2Csequence%2Clit_pubmed_id%2Cft_peptide&format=tsv&query=%28%28ft_peptide%3A%2A%29%29%20AND%20%28reviewed%3Atrue%29"
url_signal = "https://rest.uniprot.org/uniprotkb/stream?fields=accession%2Csequence%2Clit_pubmed_id%2Cft_signal&format=tsv&query=%28%28ft_signal_exp%3A%2A%29%29"
url_propeptide = "https://rest.uniprot.org/uniprotkb/stream?fields=accession%2Csequence%2Clit_pubmed_id%2Cft_propep&format=tsv&query=%28%28ft_propep_exp%3A%2A%29%29"
url_transit = "https://rest.uniprot.org/uniprotkb/stream?fields=accession%2Csequence%2Clit_pubmed_id%2Cft_transit&format=tsv&query=%28%28ft_transit%3A%2A%29%29%20AND%20%28reviewed%3Atrue%29"

res = requests.get(url_full).text
with open(raw_data+"/swissprot.tsv", mode="w", encoding="utf-8") as file:
    file.write(res)


res = requests.get(url_peptides).text
with open(raw_data+"/peptide.tsv", mode="w", encoding="utf-8") as file:
    file.write(res)

res = requests.get(url_propeptide).text
with open(raw_data+"/propeptide.tsv", mode="w", encoding="utf-8") as file:
    file.write(res)

res = requests.get(url_signal).text
with open(raw_data+"/signal.tsv", mode="w", encoding="utf-8") as file:
    file.write(res)

res = requests.get(url_transit).text
with open(raw_data+"/transit.tsv", mode="w", encoding="utf-8") as file:
    file.write(res)