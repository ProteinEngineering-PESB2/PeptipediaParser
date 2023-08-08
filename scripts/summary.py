import pandas as pd
all_peptides = pd.read_csv("../output/all_peptides.csv")
all_activity = pd.read_csv("../output/activity_pivoted.csv")
canons = all_peptides[all_peptides.is_canon]
not_canons = all_peptides[~all_peptides.is_canon]
activity_canon = all_activity[all_activity["is_canon"]]
activity_not_canon = all_activity[~all_activity["is_canon"]]
data = [
    [len(not_canons), len(canons), len(all_peptides)],
    [len(activity_not_canon), len(activity_canon), len(all_activity)],
    [len(not_canons) - len(activity_not_canon), len(canons) - len(activity_canon), len(all_peptides) - len(all_activity)]
]
df = pd.DataFrame(data, columns=["not_canon", "canon", "all"], index=["all", "activity", "without_activity"])
print(df)

df.to_csv("../output/summary.csv")