from generic_getter import getter
filenames = ["acp240.txt", "acp740.txt"]
urls = [f"https://raw.githubusercontent.com/haichengyi/ACP-DL/master/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/acp_dl/")