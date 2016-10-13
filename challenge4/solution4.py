import sys
import string
import frequencies
import binascii
from solution3 import freqDecode

# save all the high scores and then get the max score to find winning string

def decrypt(file):
    with open(str(file), "rb") as f, open("result", "a") as g:

        while True:
            results = []

            # readline() caused unhexlify() in solution3 file to throw oddlength error
            for line in f:
                result = freqDecode(line.strip())
                results.append(result)

            winner = max(results, key=lambda result: result[0])

            print(f'The highest score was: {winner[0]}')
            print(f'The key was: {winner[1]}')
            print(f'The plaintext is: {winner[2]}')

            if not f.read(1):
                break
    f.close()
    g.close()

decrypt("4.txt")