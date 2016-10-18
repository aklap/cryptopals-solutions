import sys
import frequencies
from solution3 import freq_decode

# save all the high scores and then get the max score to find winning string

def find_xor(file):
    with open(str(file), "rb") as f:

        while True:
            results = [freq_decode(line.strip()) for line in f]
            winner = max(results, key=lambda result: result[0])

            return (winner)
            break
    f.close()

