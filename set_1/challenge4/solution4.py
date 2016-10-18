import sys
import frequencies
from solution3 import freq_decode

# save all the high scores and then get the max score to find winning string

def decrypt(file):
    with open(str(file), "rb") as f:

        while True:
            results = []

            # readline() caused unhexlify() in solution3 file to throw odd length error
            for line in f:
                result = freq_decode(line.strip())
                results.append(result)

            winner = max(results, key=lambda result: result[0])

            print(f'The highest score was: {winner[0]}')
            print(f'The key was: {winner[1]}')
            print(f'The plaintext is: {winner[2]}')

            return (winner)

            if not f.read(1):
                break
    f.close()
