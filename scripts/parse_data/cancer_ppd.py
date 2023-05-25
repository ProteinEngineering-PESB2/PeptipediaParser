import pandas as pd
a = pd.read_csv("../../raw_data/cancer_ppd/mix_natural.txt", sep="\t", engine="python")
a["activity"] = "anticancer"
a = a.dropna()
a = a.rename(columns={"Sequence": "sequence"})
a = a[["sequence", "activity"]]
print(a)
a.to_csv("../parsed_data/cancer_ppd.csv", index=False)