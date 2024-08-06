#Signal Sequence
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
try:
    df = pd.read_csv(f"{raw_folder}/signalpeptide/signalpeptide.csv")
    df = df[["Signal Sequence"]].rename(columns={"Signal Sequence": "sequence"})
    df["activity"] = "signal"
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/signalpeptide.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)