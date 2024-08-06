import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    df = pd.read_csv(f"{raw_folder}/dadp/dadp.csv")
    df = df[["Bioactive sequence"]].rename(columns={"Bioactive sequence": "sequence"})
    df["activity"] = "anuran defense"
    df = df[df["sequence"] != "/"]
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/dadp.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)