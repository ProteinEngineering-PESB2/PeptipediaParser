import pandas as pd
from Bio import SeqIO
from utils import raw_folder, parse_df, parsed_folder
import os
def parse_tsv(sequence, peptide_pos):
    positions = peptide_pos.split(" ")[1].split(";")[0]
    positions = positions.split("..")
    try:
        sequence = sequence[int(positions[0])-1: int(positions[1])+1]
        return sequence
    except:
        return None
def get_id(id):
    return id.split("|")[1]
try:
    swissprot = pd.read_csv(f"{raw_folder}/swissprot/swissprot.tsv", sep="\t")
    swissprot["sequence"] = swissprot["Sequence"]
    swissprot["swissprot_id"] = swissprot["Entry"]
    swissprot = swissprot.rename(columns={"PubMed ID": "pubmed"})
    swissprot.pubmed = swissprot.pubmed.str.split(";")
    swissprot = swissprot.explode("pubmed")
    swissprot.pubmed = swissprot.pubmed.str.strip()
    swissprot = swissprot.dropna(subset=["swissprot_id", "sequence"])
    swissprot = swissprot[["swissprot_id", "sequence", "pubmed"]]

    peptides = pd.read_csv(f"{raw_folder}/swissprot/peptide.tsv", sep="\t")
    peptides["sequence"] = peptides.apply(lambda x: parse_tsv(x["Sequence"], x["Peptide"]) ,axis = 1)
    peptides["swissprot_id"] = peptides["Entry"]
    peptides = peptides.rename(columns={"PubMed ID": "pubmed"})
    peptides.pubmed = peptides.pubmed.str.split(";")
    peptides = peptides.explode("pubmed")
    peptides.pubmed = peptides.pubmed.str.strip()
    peptides = peptides.dropna(subset=["swissprot_id", "sequence"])
    peptides = peptides[["swissprot_id", "sequence", "pubmed"]]

    propeptide = pd.read_csv(f"{raw_folder}/swissprot/propeptide.tsv", sep="\t")
    propeptide["sequence"] = propeptide.apply(lambda x: parse_tsv(x["Sequence"], x["Propeptide"]) ,axis = 1)
    propeptide["swissprot_id"] = propeptide["Entry"]
    propeptide = propeptide.rename(columns={"PubMed ID": "pubmed"})
    propeptide.pubmed = propeptide.pubmed.str.split(";")
    propeptide = propeptide.explode("pubmed")
    propeptide.pubmed = propeptide.pubmed.str.strip()
    propeptide = propeptide.dropna(subset=["swissprot_id", "sequence"])
    propeptide["activity"] = "propeptide"
    propeptide = propeptide[["swissprot_id", "sequence", "pubmed", "activity"]]
    
    signal = pd.read_csv(f"{raw_folder}/swissprot/signal.tsv", sep="\t")
    signal["sequence"] = signal.apply(lambda x: parse_tsv(x["Sequence"], x["Signal peptide"]), axis = 1)
    signal["swissprot_id"] = signal["Entry"]
    signal = signal.rename(columns={"PubMed ID": "pubmed"})
    signal.pubmed = signal.pubmed.str.split(";")
    signal = signal.explode("pubmed")
    signal.pubmed = signal.pubmed.str.strip()
    signal = signal.dropna(subset=["swissprot_id", "sequence"])
    signal["activity"] = "signal"
    signal = signal[["swissprot_id", "sequence", "pubmed", "activity"]]

    transit = pd.read_csv(f"{raw_folder}/swissprot/transit.tsv", sep="\t")
    transit["sequence"] = transit.apply(lambda x: parse_tsv(x["Sequence"], x["Transit peptide"]), axis = 1)
    transit["swissprot_id"] = transit["Entry"]
    transit = transit.rename(columns={"PubMed ID": "pubmed"})
    transit.pubmed = transit.pubmed.str.split(";")
    transit = transit.explode("pubmed")
    transit.pubmed = transit.pubmed.str.strip()
    transit = transit.dropna(subset=["swissprot_id", "sequence"])
    transit["activity"] = "transit"
    transit = transit[["swissprot_id", "sequence", "pubmed", "activity"]]

    df = pd.concat([ swissprot, peptides, propeptide, signal, transit])
    df = df.drop_duplicates()
    df = df.dropna(subset=["sequence"])

    df = parse_df(df)
    df.to_csv(f"{parsed_folder}/swissprot.csv", index=False)
    print(os.path.basename(__file__), "success")
    
except Exception as e:
    print(__file__, e)