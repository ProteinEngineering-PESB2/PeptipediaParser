from Bio import SeqIO
import pandas as pd
import os
from utils import raw_folder, parse_df, parsed_folder
try:
    records = SeqIO.parse(f"{raw_folder}/conoserver/conoserver_protein.fa", "fasta")
    df = [[str(record.description), str(record.seq)] for record in records]
    df = pd.DataFrame(df, columns=["description", "sequence"])
    df["activity"] = df.description.str.contains("toxin")
    df = df.replace(True, "toxic")
    df = df.replace(False, None)
    df = df[["sequence", "activity"]]
    df = df.dropna(subset=["sequence"])
    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/conoserver.csv", index=False)
    print(os.path.basename(__file__), "success")
except Exception as e:
    print(__file__, e)