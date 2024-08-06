from generic_getter import getter
filenames = ["pos_train", "pos_test"]
urls = [f"https://webs.iiitd.edu.in/raghava/cellppdmod/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/cellppd_mod/")