from generic_getter import getter
filenames = ["pos-maindataset-1", "pos-indep-1"]
urls = [f"https://webs.iiitd.edu.in/raghava/toxinpred/datasets/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/toxinpred/")