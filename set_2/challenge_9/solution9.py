
 # creating a plaintext that is an even multiple of the blocksize
 
def pad_to(block, n, padded=[]):
    if len(block) == n:
        padded.append(block)
    elif len(block) < n:
        while len(block) < n:
            block += '\x04'
        padded.append(block)
    elif len(block) > n:
        padded.append(block[0:n])
        return pad_to(block[n:], n, padded)

    return padded

