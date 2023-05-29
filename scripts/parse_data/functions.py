aminoacids = "ARNDBCEQZGHILKMFPSTWYVarndbceqzghilkmfpstwyv"
def verify_sequences(sequence):
    if len(sequence) > 150:
        return None
    for res in sequence:
        if res not in aminoacids:
            return None
    return sequence.upper()