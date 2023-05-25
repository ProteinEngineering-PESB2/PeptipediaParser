import pandas as pd
a = pd.read_excel("../../raw_data/neuropedia/Database_NeuroPedia_063011.xls", skiprows=1)
a["sequence"] = a[["Amino acid Sequence"]]
a = a[["sequence"]]
a[["activity"]] = "neuropeptide"
a = a.drop_duplicates()
a.to_csv(".././parsed_data/neuropedia.csv", index=False)