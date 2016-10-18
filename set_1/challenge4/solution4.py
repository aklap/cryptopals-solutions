import sys
sys.path.append('../challenge3')
from solution3 import decrypt_xor

# save all the high scores and then get the max score to find winning string

def find_xor(file):
    with open(str(file), "rb") as f:

        while True:
            results = [decrypt_xor(line.strip()) for line in f]
            best_match = max(results, key=lambda result: result[0])
            return (best_match)
    f.close()

