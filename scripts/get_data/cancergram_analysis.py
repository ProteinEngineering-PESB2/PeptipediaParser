from generic_getter import getter
filenames = ["pos_test_main.txt",
             "neg_test_alternate.txt",
             "neg_test_main.txt",
             "pos_train_main.txt",
             "neg_train_alternate.txt",
             "neg_train_main.txt",
             "pos_test_alternate.txt",
             "pos_train_alternate.txt"]
urls = [f"https://raw.githubusercontent.com/BioGenies/CancerGram-analysis/master/data/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/cancergram_analysis/")