from generic_getter import getter
files = ["AMPlify_AMP_test_common.fa", "AMPlify_AMP_train_common.fa"]
urls = [f"https://raw.githubusercontent.com/bcgsc/AMPlify/master/data/{file}" for file in files]
getter(urls, raw_folder = "../../raw_data/amplify/")