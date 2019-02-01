import sys
sys.path.append('../challenge3')
from solution3 import xor_bytes
from frequencies import *
import binascii


def find_xor(file):
    """Find encrypted string in file."""
    with open(file) as f:
        text_bytes = binascii.unhexlify(line.strip())
        xor_results = [xor_bytes(text_bytes) for line in f]
        scored = [find_match(res) for res in xor_results]
        best_match = max(scored, key=lambda result: result[0])

        return best_match[2]
