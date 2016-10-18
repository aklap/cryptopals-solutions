import sys
import base64
from keys import KEYSIZE
from functools import reduce
sys.path.append('../challenge3')
from solution3 import decrypt_xor
from frequencies import score
sys.path.append('../challenge5')
from solution5 import xor_encrypt as to_plaintext
from distance_functions import *
from transform_functions import *

def break_repeating(filename):
    with open(str(filename), "rb") as f:
        ciphertext = base64.b64decode(f.read())
        distances = []
        key = ''
        max_key_score = 0

        for k_size in KEYSIZE:
        # normalize hamming distances, get average distance of the first 2 chunks
            pair = to_chunks(ciphertext, k_size)[0:2]
            normalized_distance = normalize(pair, k_size)
            distances.append((k_size, normalized_distance))

        # sort the distances tuples by lowest to highest distance
        distances = sorted(distances, key=lambda dist: dist[1])

        for dist in distances:
            k_length = dist[0]
            cipher_key = []

            # transpose all the blocks
            ciphertext_blocks = to_chunks(ciphertext, k_length)
            transposed = transpose(ciphertext_blocks, k_length)
            
            # break as if single character XOR to get each char of the key string
            for block in transposed:
                cipher_key.append(decrypt_xor(reduce(lambda a,b: a+b, block))[1])

            # show all the possible key strings for each keysize length, sorted lowest to highest hamming distances
            if len(''.join(cipher_key)) > 1 and score(''.join(cipher_key)) > max_key_score:
                max_key_score = score(''.join(cipher_key))
                key = ''.join(cipher_key)
        
        return (key, to_plaintext(ciphertext, key))
