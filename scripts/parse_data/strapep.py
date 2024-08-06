import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    df = pd.read_csv(f"{raw_folder}/strapep/data.csv")
    df = df[["Sequence", "Classification"]].rename(columns={"Classification": "activity", "Sequence": "sequence"})
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/strapep.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)