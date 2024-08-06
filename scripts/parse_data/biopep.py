import pandas as pd
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    df = pd.read_csv(f"{raw_folder}/biopep/biopep.csv")
    df = df[["Sequence", "Activity"]]
    df = df.rename(columns={"Sequence": "sequence", "Activity": "activity"})
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/biopep.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)
