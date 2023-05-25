from generic_getter import getter
files = ["acp164.fa", "acp240.fa", "acp500.fa", "acp740.fa"]
urls = [f"https://raw.githubusercontent.com/mrzResearchArena/Anticancer-Peptides-CNN/master/Datasets-FASTA/{file}" for file in files]
getter(urls, raw_folder = "../../raw_data/anticancer_peptides_cnn")