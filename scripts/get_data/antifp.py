from generic_getter import getter
filenames = ["pos_train_ds1", "pos_test_ds1"]
urls = [f"https://webs.iiitd.edu.in/raghava/antifp/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/antifp/")