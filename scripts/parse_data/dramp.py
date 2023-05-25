import pandas as pd
df = pd.read_excel("../../raw_data/dramp/general_amps.xlsx")
a = df[["Sequence", "Activity"]]
a.Activity = a.Activity.str.replace(" ", "")
a.Activity = a.Activity.str.split(",")
a = a.explode("Activity")
print(a)
a.to_csv("../../parsed_data/dramp.csv", index=False)