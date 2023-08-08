import pandas as pd
from Bio import SeqIO
from functions import verify_sequences

def parse_tsv(sequence, peptide_pos):
    positions = peptide_pos.split(" ")[1].split(";")[0]
    positions = positions.split("..")
    try:
        sequence = sequence[int(positions[0])-1: int(positions[1])+1]
        return sequence
    except:
        return None
pdb_path = "../../raw_data/swissprot/uniprot_sprot.fasta"
df = pd.DataFrame([[a.description, str(a.seq)] for a in list(SeqIO.parse(pdb_path, "fasta"))], columns=["id", "sequence"])
df = df[["sequence"]]
df = df.dropna(subset=["sequence"])
df = df.drop_duplicates()

peptides = pd.read_csv("../../raw_data/swissprot/peptide.tsv", sep="\t")
peptides["sequence"] = peptides.apply(lambda x: parse_tsv(x["Sequence"], x["Peptide"]) ,axis = 1)
peptides = peptides.dropna()
peptides = peptides[["sequence"]]

propeptide = pd.read_csv("../../raw_data/swissprot/propeptide.tsv", sep="\t")
propeptide["sequence"] = propeptide.apply(lambda x: parse_tsv(x["Sequence"], x["Propeptide"]) ,axis = 1)
propeptide = propeptide.dropna()
propeptide["activity"] = "propeptide"
propeptide = propeptide[["sequence", "activity"]]

signal = pd.read_csv("../../raw_data/swissprot/signal.tsv", sep="\t")
signal["sequence"] = signal.apply(lambda x: parse_tsv(x["Sequence"], x["Signal peptide"]), axis = 1)
signal = signal.dropna()
signal["activity"] = "signal"
signal = signal[["sequence", "activity"]]

transit = pd.read_csv("../../raw_data/swissprot/transit.tsv", sep="\t")
transit["sequence"] = transit.apply(lambda x: parse_tsv(x["Sequence"], x["Transit peptide"]), axis = 1)
transit = transit.dropna()
transit["activity"] = "transit"
transit = transit[["sequence", "activity"]]

df = pd.concat([df, peptides, propeptide, signal, transit])
df = df.drop_duplicates()
df = df.dropna(subset=["sequence"])

df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))
df = df.dropna(subset=["sequence"])
print(df)
df.to_csv("../../parsed_data/swissprot.csv", index=False)