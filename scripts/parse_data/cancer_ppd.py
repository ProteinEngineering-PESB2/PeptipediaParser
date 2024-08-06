import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    df = pd.read_csv(f"{raw_folder}/cancer_ppd/mix_natural.txt", sep="\t", engine="python")
    df["activity"] = "anticancer"
    df = df.dropna()
    df = df.rename(columns={"Sequence": "sequence"})
    df = df[["sequence", "activity"]]
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/cancer_ppd.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)
