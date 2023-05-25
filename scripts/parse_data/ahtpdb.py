import pandas as pd
from os.path import basename
import os
from config import *

script_name = basename(__file__.split(".")[0])
raw_folder = RAW_FOLDER.format(script_name)
dfs = []
for filename in os.listdir(raw_folder):
    path = os.path.join(raw_folder, filename)
    data = pd.read_csv(path, sep="\t")
    data = data[["seq "]]
    data["activity"] = "anti-hipertensive"
    data = data.rename(columns={"seq ": "sequence"})
    dfs.append(data)
df = pd.concat(dfs)
df = df.drop_duplicates()
print(df)
df.to_csv(os.path.join(PARSED_FOLDER, script_name + ".csv"), index=False)
