#https://raw.githubusercontent.com/guofei-tju/Ensemble-classifier-chain-model/master/Dataset/original/pos_training.txt
#https://raw.githubusercontent.com/guofei-tju/Ensemble-classifier-chain-model/master/Dataset/original/pos_validation.txt
from generic_getter import getter
filenames = ["pos_training.txt", "pos_validation.txt"]
urls = [f"https://raw.githubusercontent.com/guofei-tju/Ensemble-classifier-chain-model/master/Dataset/original/{file}" for file in filenames]
getter(urls, "../../raw_data/ensemble_chassifier_chain_model/")