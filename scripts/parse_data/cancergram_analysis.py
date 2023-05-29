import pandas as pd
from functions import verify_sequences
raw_folder = "../../raw_data/cancergram_analysis/"
a = pd.read_csv(f"{raw_folder}/pos_test_main.txt", header=None)
b = pd.read_csv(f"{raw_folder}/pos_train_main.txt", header=None)
c = pd.read_csv(f"{raw_folder}/pos_test_alternate.txt", header=None)
d = pd.read_csv(f"{raw_folder}/pos_train_alternate.txt", header=None)

e = pd.read_csv(f"{raw_folder}/neg_test_alternate.txt", header=None)
f = pd.read_csv(f"{raw_folder}/neg_test_main.txt", header=None)
g = pd.read_csv(f"{raw_folder}/neg_train_alternate.txt", header=None)
h = pd.read_csv(f"{raw_folder}/neg_train_main.txt", header=None)
anticancer = pd.concat([a, b, c, d])
anticancer["activity"] = "anticancer"

amp = pd.concat([e, f, g, h])
amp["activity"] = "antimicrobial"
df = pd.concat([anticancer, amp])
df = df.rename(columns={0: "sequence"})
df = df.dropna(subset=["sequence"])
df["sequence"] = df["sequence"].map(verify_sequences)
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()
print(df)
df.to_csv("../../parsed_data/cancergram_analysis.csv", index=False)