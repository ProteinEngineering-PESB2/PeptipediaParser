from generic_getter import getter
filenames = ["pos_train_main", "pos_test_main", "pos_train_alternate", "pos_test_alternate"]
urls = [f"https://webs.iiitd.edu.in/raghava/anticp2/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/anticp2/")