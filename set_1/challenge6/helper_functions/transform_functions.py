def transpose(blocks, k):
    transposed = []
    for i in range(0, k):
        transposed.append([block[i:i+1] for index, block in enumerate(blocks)])
    return transposed

# gets chunks of k-sized blocks
def to_chunks(string, k):
    start = 0
    return [string[i:i+k] for i in range(0, len(string), k)]
