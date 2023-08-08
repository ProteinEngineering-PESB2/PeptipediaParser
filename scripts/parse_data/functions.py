aminoacids = "ARNDBCEQZGHILKMFPSTWYVarndbceqzghilkmfpstwyv"
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