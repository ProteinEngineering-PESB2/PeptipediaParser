import pandas as pd
df = pd.read_csv("../../auxiliar_data/predictive_models.csv")
activity = pd.read_csv("../../tables/activity.csv")
a = df.merge(activity, left_on="activity", right_on="name", how="left")
a = a[["id_activity", "algorithm","encoder"]]
a = a.sort_values(by=["id_activity"])
a.to_csv("../../tables/predictive_model.csv", index=False)
