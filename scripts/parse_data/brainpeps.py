import pandas as pd
df = pd.read_csv("../../raw_data/brainpeps/brainpeps.csv")
df["activity"] = "brain-blood-barrier"
df.to_csv("../../parsed_data/brainpeps.csv", index=False)