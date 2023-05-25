from generic_getter import getter
files = ["AMP.tr.fa", "AMP.eval.fa", "AMP.te.fa"]
urls = [f"https://raw.githubusercontent.com/zhanglabNKU/APIN/master/data/{file}" for file in files]
getter(urls, raw_folder = "../../raw_data/apin/")