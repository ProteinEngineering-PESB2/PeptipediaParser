import os
import pandas as pd
#Folders
parsed_data_folder = "../../parsed_data"
aux_data_folder = "../../auxiliar_data"
output_folder = "../../output"

#Recorre todos los csv de parsed data y los concatena
dfs = []
for file in os.listdir(parsed_data_folder):
    path = os.path.join(parsed_data_folder, file)
    db = pd.read_csv(path)
    db["source"] = file.split(".")[0]
    dfs.append(db)
df = pd.concat(dfs)

df = df.replace("", None) #Transforma a NaN los strings vacíos 
df.sequence = df.sequence.str.strip()
df.activity = df.activity.str.lower() #Activities todos quedan en lower
nutraceutical = df[df.activity == "nutraceutical"][["sequence"]]
nutraceutical["nutraceutical"] = True #Field is nutraceutical

activities = pd.read_csv(f"{aux_data_folder}/activity_replacement.csv") #Activity replacement to common names
df = df.merge(activities, on="activity", how="outer")
df.activity = df.activity.replace("", None)
df.sequence = df.sequence.replace("", None)
df = df.dropna(subset="sequence")
unique_sequences = df.drop_duplicates(subset="sequence")[["sequence"]].reset_index(drop=True)

unique_sequences["id_sequence"] = unique_sequences.index + 1
df = unique_sequences.merge(df, on="sequence", how="outer")
df = df.rename(columns={"activity": "keyword", "Proposal activity": "activity"}) #Keywords and Activities.
df = df.merge(nutraceutical, on="sequence", how="left")
df.nutraceutical = df.nutraceutical.fillna(False)
df.to_csv(f"{output_folder}/all_data.csv", index=False) #All data contains all info.

df_act = df[df.activity.notna()]
df_act.to_csv(f"{output_folder}/all_data_act.csv", index=False) #Separates if has activity

df_non_act = df[df.activity.isna()]
df_non_act.to_csv(f"{output_folder}/all_data_non_act.csv", index=False)#Separates if doesn't has activity