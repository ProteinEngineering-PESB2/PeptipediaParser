aminoacids = "ARNDCEQGHILKMFPSTWYVarndceqghilkmfpstwyv"
raw_folder = "../../raw_data/"
parsed_folder = "../../parsed_data/"


def verify_sequences(sequence):
    sequence = sequence.strip()
    is_canon = True
    for res in sequence:
        if res not in aminoacids:
            is_canon = False
            
    if is_canon:
        if len(sequence) > 150:
            return None, None
        if len(sequence) <= 1:
            return None, None
        sequence = sequence.upper().strip()
    return sequence, is_canon

def get_patent(description):
    if "US " in description:
        return "US " + description.split("US ")[1]
    
def parse_df(df):
    df["sequence"], df["is_canon"] = zip(*df["sequence"].map(verify_sequences))

    df = df.dropna(subset=["sequence"])
    df = df.drop_duplicates()
    return df

def separate_pubmed_patent(row):
    try:
        if "US" in row:
            return [None, "US" + row.split("US")[1]]
        return [row, None]
    except:
        return [None, None]