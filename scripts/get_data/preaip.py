from generic_getter import getter
filenames = ["training-positive.txt", "test-positive.txt"]
urls = [f"http://kurata14.bio.kyutech.ac.jp/PreAIP/downloads/{file}" for file in filenames]
getter(urls, "../../raw_data/preaip/")