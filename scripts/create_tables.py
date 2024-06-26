import pandas as pd

peptides = pd.read_csv("../output/all_peptides.csv")
previous_peptides = pd.read_csv("../previous_data/peptide_202306291502.csv").drop(columns=["moonlight", "structure", "is_aa_seq", "ic50_value", "ic50_unit", "ic50_description"])
peptides = peptides.merge(previous_peptides, on="sequence", how="left")
peptides = peptides.drop(columns=["idpeptide"])
print(peptides)
peptides.rename(columns={"id": "id_peptide"}).to_csv("../tables/peptide.csv", index=False)

"""
previous_go = pd.read_csv("../previous_data/gene_ontology_202307071329.csv")
previous_go.to_csv("../tables/gene_ontology.csv", index=False)

previous_phgo = pd.read_csv("../previous_data/peptide_has_go_202307071330.csv")
previous_phgo = previous_phgo[previous_phgo["probability"] >=0.38]
previous_phgo = previous_peptides[["idpeptide", "sequence"]].merge(previous_phgo, on="idpeptide")
phgo = peptides.merge(previous_phgo, on="sequence")[["id", "id_go"]]
print(phgo)
phgo.rename(columns={"id": "id_peptide"}).to_csv("../tables/peptide_has_go.csv", index=False)
"""

peptipedia_data = pd.read_csv("../output/peptipedia_data.csv")
sources = peptipedia_data[["source"]].drop_duplicates().reset_index(drop=True)
sources["id_source"] = sources.index + 1
sources = sources.rename(columns={"source": "name"})
sources.to_csv("../tables/source.csv", index=False)
peptipedia_data = peptipedia_data.merge(sources, left_on="source", right_on="name")
phs = peptipedia_data[["id", "id_source"]].drop_duplicates()
phs.rename(columns={"id": "id_peptide"}).to_csv("../tables/peptide_has_source.csv", index=False)

activities = pd.read_csv("../output/activities_count.csv")
activities = activities.rename(columns={"activity": "name"})[["name"]]

activities["id_activity"] = activities.index + 1
descriptions = pd.read_csv("./descriptions.csv")
print(activities)
print(descriptions)
activities = activities.merge(descriptions, on="name")
print(activities)

activities.to_csv("../tables/activity.csv", index=False)

pivoted = pd.read_csv("../output/activity_pivoted.csv")
peptides = peptides.rename(columns={"id": "id_peptide"})
pivoted = pivoted.merge(peptides, on="sequence")
melted = pivoted.melt(id_vars=["sequence", "id_peptide"], var_name="activity")
melted = melted[melted.value == 1][["id_peptide", "activity"]]
melted = melted.merge(activities, left_on="activity", right_on="name")[["id_peptide", "id_activity"]].drop_duplicates()
melted.to_csv("../tables/peptide_has_activity.csv", index=False)