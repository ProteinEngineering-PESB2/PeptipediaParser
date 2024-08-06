"""Anti cancer peptides CNN"""
import os
from Bio import SeqIO
import pandas as pd
from utils import parse_df, parsed_folder, raw_folder
try:
    raw_folder = f"{raw_folder}/anticancer_peptides_cnn/"
    full_data = []
    for filename in os.listdir(raw_folder):
        path = os.path.join(raw_folder, filename)
        data = [[str(a.seq), a.description.split("|")[1]]
                for a in list(
                    SeqIO.parse(path, "fasta"))]
        df = pd.DataFrame(data, columns=["sequence", "activity"])
        full_data.append(df)
    df = pd.concat(full_data)
    df = df[df.activity == "1"]
    df["activity"] = "anticancer"
    df = parse_df(df)
    df.to_csv(os.path.join(f"{parsed_folder}/anticancer_peptides_cnn.csv"), index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)