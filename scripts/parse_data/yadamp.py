import pandas as pd
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    df = pd.read_csv(f"{raw_folder}/yadamp/data.csv")
    df = df[df["0"].str.contains("SEQ")][["0"]]
    df = df.rename(columns={"0": "sequence"})
    df["sequence"] = df["sequence"].replace("SEQ: ", "", regex=True)
    df["activity"] = "antimicrobial"
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/yadamp.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)