from os import listdir
import pandas as pd
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    full_data = []
    raw_folder = f"{raw_folder}/satpdb/"
    dfs = []
    for filename in listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        with open(path, encoding="utf-8", mode="r") as file:
            text = file.read()
        sequences = ["".join(a.split("\n")[1:]) for a in text.split(">")]
        df = pd.DataFrame()
        df["sequence"] = sequences
        df["activity"] = filename.replace(".fasta", "")
        dfs.append(df)
    df = pd.concat(dfs)
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/satpdb.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)