import pandas as pd
import jellyfish
from config import *
from os.path import basename
import os
activities = pd.read_csv("../activities.csv")["name"]

script_name = basename(__file__.split(".")[0])
raw_folder = RAW_FOLDER.format(script_name)
def find_similar_words(phrase):
    selected_activities = ["antitubercular"]
    for word in phrase:
        for act in activities:
            distance = jellyfish.jaro_distance(word, act)
            if distance > 0.8:
                selected_activities.append(act)
    return list(set(selected_activities))

def merge_words(phrase):
    return phrase.lower().replace("anti ", "anti").replace("gram ", "gram-")

raw_folder = RAW_FOLDER.format(basename(__file__).split('.')[0])

df = pd.read_csv(raw_folder + "/data.csv")
df = df[["Sequence", "Other Activities"]]

df = df.drop_duplicates()

df["Other Activities"] = df["Other Activities"].map(merge_words, na_action='ignore')
df["Other Activities"] = df["Other Activities"].str.split()
df["Other Activities"] = df["Other Activities"].map(find_similar_words, na_action='ignore')
df = df.explode("Other Activities")
df = df.drop_duplicates()
df = df.rename(columns={"Sequence": "sequence", "Other Activities": "activity"})
print(df)
df.to_csv(os.path.join(PARSED_FOLDER, script_name + ".csv"), index=False)
