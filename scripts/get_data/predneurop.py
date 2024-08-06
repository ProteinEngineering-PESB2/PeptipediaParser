#https://raw.githubusercontent.com/xialab-ahu/PredNeuroP/master/datasets/Pos_test_fasta.txt
from generic_getter import getter
filenames = ["Pos_test_fasta.txt", "Pos_train_fasta.txt"]
urls = [f"https://raw.githubusercontent.com/xialab-ahu/PredNeuroP/master/datasets/{file}" for file in filenames]
getter(urls, "../../raw_data/predneurop/")