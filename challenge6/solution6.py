
from functools import reduce
import base64
import sys
sys.path.append('../challenge3')
from solution3 import freq_decode
from frequencies_6 import score

def break_xor(filename):
    with open(str(filename), "rb") as f:
        # decode from base64
        ciphertext = base64.b64decode(f.read())
        KEYSIZE = range(1,40)
        distances = []

        for k in KEYSIZE:
            print(f'For key {k}')

        # normalize hamming distances, get average distance of the first 4 chunks
            pair = to_chunks(ciphertext, k)[0:2]
            normalized_distance = normalize(pair, k)
            distances.append((k, normalized_distance))

        distances = sorted(distances, key=lambda dist: dist[1])

        for tup in distances:
            key_n = tup[0]
            print(key_n)
            key_string = []

            ciphertext_blocks = to_chunks(ciphertext, key_n)
        
            # transpose all the blocks
            transposed = []
            for i in range(0, key_n):
                transposed.append(([block[i:i+1] for index, block in enumerate(ciphertext_blocks)]))

            #break as if single character XOR to get each char of the key string
            for block in transposed:
                key_string.append(freq_decode(reduce(lambda a,b: a+b, block))[1])
            # show all the possible key strings for each keysize length, sorted lowest to highest hamming distances
            print(''.join(key_string))

def normalize(pair, k):
    distance = hamming(pair[0].decode(), pair[1].decode())
    return distance/k

def hamming(string1, string2):
    distances = []

    for i, char in enumerate(string1):
        xbyte = bin(ord(char)^ord(string2[i]))
        distances.append(xbyte.count('1'))
    return (reduce(lambda a,b: a+b, distances))

def to_chunks(string, k):
    start = 0
    # gets chunks of n-sized blocks
    return [string[i:i+k] for i in range(0, len(string), k)]

break_xor('ciphertext.txt')
