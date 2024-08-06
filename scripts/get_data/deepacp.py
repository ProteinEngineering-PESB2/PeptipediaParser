from generic_getter import getter
filenames = ["ACPs10.txt", "ACPs250.txt", "ACPs82.txt"]
urls = [f"https://raw.githubusercontent.com/jingry/autoBioSeqpy/master/examples/anticancer_peptide_prediction/data/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/deepacp/")