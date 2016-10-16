
from functools import reduce
import sys
import base64
import sys
sys.path.append('../challenge3')
from solution3 import freq_decode

def break_xor(filename):
    with open(str(filename), "rb") as f:
        # decode from base64
        ciphertext = base64.b64decode(f.read())
        KEYSIZE = range(2,15)
        distances = list()

        for n in KEYSIZE:
            # print(f'For key {n}')
            string1 = ciphertext[:n].decode()
            string2 = ciphertext[n :n+n].decode()
            normalized_hamming = (hamming(string1, string2)/n)
            distances.append(normalized_hamming)
        # find the key which is the keysize with the lowest normalized hamming distance
        lowest_hamming = min(distances)    
        key = KEYSIZE[distances.index(lowest_hamming)]
        ciphertext_blocks = to_chunks(ciphertext, key)
        
        #transpose all the blocks
        transposed = []
        for i in range(0, key):
            transposed.append(([block[i:i+1] for index, block in enumerate(ciphertext_blocks)]))
        print(transposed)

def hamming(string1, string2):
    distances = []

    for i, char in enumerate(string1):
        char_1 = char
        char_2 = string2[i]
        # xor the bits in each byte, returning everthing after the binary prefix of 0b as a string
        xbyte = bin(ord(char_1)^ord(char_2))
        # count the differences by counting the occurrences of the 1 add onto count
        hamming_distance = xbyte.count('1')
        distances.append(hamming_distance)

    return reduce(lambda a,b: a+b, distances)

def to_chunks(string, n):
    start = 0
    return [string[i:i + n] for i in range(0, len(string), n)]

break_xor('ciphertext.txt')
