from generic_getter import getter
filenames = ["d_natural.txt", "mix_natural.txt", "l_natural.txt"]
urls = [f"http://crdd.osdd.net/raghava/cancerppd/natural_seq_dwn/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/cancer_ppd/")