from generic_getter import getter
files = ["long.txt", "small.txt", "pepic50.txt"]
urls = [f"http://crdd.osdd.net/raghava/ahtpdb/downloads/{file}" for file in files]
getter(urls, raw_folder = "../../raw_data/ahtpdb/")