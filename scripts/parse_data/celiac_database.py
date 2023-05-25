import pandas as pd

celiac = pd.read_csv("../../raw_data/allergenonline/Celiac Database.csv")
celiac = celiac[["Sequence", "Toxicity"]]
celiac = celiac.rename(columns={"Sequence": "sequence", "Toxicity": "activity"})
celiac["activity"] = celiac["activity"] + "-celiac"
celiac.to_csv("../../parsed_data/celiac_database.csv", index=False)