import pandas as pd

df = pd.read_csv("../../auxiliar_data/predicted_activities.csv") #reads predictions
print(df)
peptide = pd.read_csv("../../tables/peptide.csv")[["id_peptide", "sequence"]]
activity = pd.read_csv("../../tables/activity.csv")[["id_activity", "name"]]
merged = []
for i in range(114): #Chunks
    print(i)
    a = df[1000000*i:1000000*(i+1)]
    a = a.merge(peptide, on="sequence", how="left")
    a = a.merge(activity, left_on="activity", right_on="name")[["id_peptide", "id_activity"]]
    a["predicted"] = True #Predicted true
    a.to_csv("../../tables/peptide_has_activity.csv", mode="a", header=False, index=False) #Appends to peptide has activity
df = pd.read_csv("../../tables/peptide_has_activity.csv")
#Checks if there are reported with same activity
df = df.drop_duplicates(subset=["id_peptide", "id_activity"], keep="first")
df.to_csv("../../tables/peptide_has_activity.csv", index=False)