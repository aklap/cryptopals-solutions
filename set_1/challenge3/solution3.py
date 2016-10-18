import binascii
from frequencies import find_match
from constants import POSSIBLE_KEYS as KEYS

# XOR the decoded bytes to get results for every possible key, use letter frequency to find likely match

def xor_bytes(text):
    results = []
    for key in KEYS:
        result = [chr(byte^ord(key)) for byte in text]
        results.append(result)
    return results

def decrypt_xor(ciphertext):
    try:
        ciphertext = binascii.unhexlify(ciphertext)
    finally:
        xor_results = xor_bytes(ciphertext)
        match = find_match(xor_results)
        best_key = KEYS[match[1]]
        score = match[0]
        plaintext = match[2]
        return (score, best_key, plaintext)
