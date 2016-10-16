import binascii
import string
from Crypto.Cipher import AES
import sys
sys.path.append('../challenge6')
from solution6 import to_chunks

def find_plaintext(file):
    with open(str(file), "rb") as f:
        while True:
            lines = f.readlines()

            for i, line in enumerate(lines):
                # strip line
                line = line.strip()

                #break each line into 16 byte (128 bit) chunks, must be a multiple of 16 bc of ECB
                chunks = to_chunks(line, 16)
                
                #create a set of *unique elements* based on that collection
                unique_chunks = set(chunks)

                # find the difference; if there are repeated chunks it's ECB because ECB repeats/doesn't have an (or even randomized) IV
                duplicates = len(chunks) - len(unique_chunks)

                # return the line and line no
                if duplicates > 0:
                    ECB_line = (i, chunks)
                    print(f'The ECB encrypted line is line no. {i}:\n\n{chunks}')
                    return (i, chunks)
                # TODO: decrypt the ECB string
            break
    f.close()
