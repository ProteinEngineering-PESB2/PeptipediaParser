import os
import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
try:
    raw_folder = f"{raw_folder}/marine_algae_derived/"
    df = pd.read_excel(raw_folder + "All Peptides_.xlsx")
    df = df[["peptide sequence", "Activity"]]
    df = df.rename(columns={"peptide sequence": "sequence", "Activity": "activity"})
    df = df.dropna(subset=["sequence"])
    df.sequence = df.sequence.str.split(", ")
    df = df.explode("sequence")
    df = parse_df(df)
    df2 = df.copy()
    df2.activity = "Nutraceutical"
    df = pd.concat([df, df2])
    df.to_csv(f"{parsed_folder}/marine_algae_derived.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)