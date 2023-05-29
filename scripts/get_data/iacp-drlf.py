from generic_getter import getter
filenames = ["ACP20AltTest.fasta", "ACP20AltTrain.fasta", "ACP20mainTest.fasta", "ACP20mainTrain.fasta"]
urls = [f"https://raw.githubusercontent.com/zhibinlv/iACP-DRLF/main/dataset/{filename}" for filename in filenames]
getter(urls, raw_folder = "../../raw_data/iacp-drlf/")