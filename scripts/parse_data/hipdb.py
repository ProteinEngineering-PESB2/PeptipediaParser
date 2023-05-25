import pandas as pd
a = pd.read_excel("../../raw_data/hipdb/HIPdb_data.xls")
a = a[["SEQUENCE"]]
a["activity"] = "antiviral"
a = a.rename(columns={"SEQUENCE": "sequence"})
a.to_csv("../../parsed_data/hipdb.csv", index=False)

print(a)