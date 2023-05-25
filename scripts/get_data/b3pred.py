from generic_getter import getter
filenames = ["Positive_B3PPs.fasta"]
urls = [f"https://webs.iiitd.edu.in/raghava/b3pred/Datasets/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/b3pred/")