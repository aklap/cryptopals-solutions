import string
import frequencies
import binascii

def freq_decode(ciphertext):
    results = []
    highest_score = 0 
    winner = ''
    plaintext = ''
    # decode from ascii to bytes
    ciphertext = binascii.unhexlify(ciphertext)
    possible_keys = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

    # XOR the decoded bytes to get results for every possible key
    for key in possible_keys:
        result = ''

        for byte in ciphertext:
            xbyte = (byte^ord(key))
            result += (chr(xbyte))
        results.append((key, result))
    # examine the frequencies of results to find best scoring match
    for i, result in enumerate(results):
        if frequencies.score(result) > highest_score:
            highest_score = frequencies.score(result)
            winner = possible_keys[i]
            plaintext = results[i]
    print(f'The highest score is {highest_score}')
    print(f'Therefore the correct key is: {winner}')
    print(f'The plaintext is: {plaintext}')


