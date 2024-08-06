import pandas as pd
from utils import raw_folder, parse_df, parsed_folder
import os
from Bio import SeqIO
try:
    raw_folder = f"{raw_folder}/dbaasp/"
    references = pd.read_csv(f"{raw_folder}/references.csv")
    datas = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        records = SeqIO.parse(path, "fasta")
        df = [[str(record.id), str(record.seq)] for record in records]
        df = pd.DataFrame(df, columns=["id", "sequence"])
        df["activity"] = filename.split(".")[0]
        datas.append(df)
    df = pd.concat(datas)
    df = parse_df(df)
    df = df.merge(references, on="id", how="left")
    df = df.drop(columns=["id"])
    df.to_csv(f"{parsed_folder}/dbaasp.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)