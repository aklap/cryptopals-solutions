import binascii
from frequencies import find_match
from constants import POSSIBLE_KEYS as KEYS

# XOR the decoded bytes to get results for every possible key, use letter frequency to find likely match

def xor_ciphertext(ciphertext):
    results = []
    for key in KEYS:
        result = [chr(byte^ord(key)) for byte in ciphertext]
        results.append(result)
    return results

def decrypt_xor(ciphertext):
    decoded_text = binascii.unhexlify(ciphertext)
    xor_results = xor_ciphertext(decoded_text)
    match = find_match(xor_results)
    best_key = KEYS[match[0]]
    plaintext = match[1]
    return (best_key, plaintext)
