#https://research.timmons.eu/static/ENNAVIA_A_dataset.fasta
from generic_getter import getter
filenames = ["ENNAVIA_A_dataset.fasta", "ENNAVIA_B_dataset.fasta", "ENNAVIA_C_dataset.fasta", "ENNAVIA_D_dataset.fasta"]
urls = [f"https://research.timmons.eu/static/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/ennavia/")