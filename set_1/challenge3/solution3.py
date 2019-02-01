import binascii
from frequencies import find_match, POSSIBLE_KEYS


def xor_bytes(text):
    """XOR text against keys and return the resulting plaintexts."""
    results = []
    for key in POSSIBLE_KEYS:
        # XOR byte sequence against key as int and get result as letter
        result = [chr(byte ^ ord(key)) for byte in text]
        # Joining gives us spaces we can split on to get separate words
        results.append(''.join(result))

    return results


def decrypt_xor(ciphertext):
    """Decrypt a ciphertext."""
    try:
        # Take hex, return binary data
        ciphertext = binascii.unhexlify(ciphertext)
    finally:
        xor_results = xor_bytes(ciphertext)
        match = find_match(xor_results)
        plaintext = match[2]

        return plaintext
