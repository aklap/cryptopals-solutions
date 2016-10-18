import sys
import binascii

def get_XOR(file1, file2):

    with open(str(file1), "rb") as a, open(str(file2), "rb") as b:

        file_a = binascii.unhexlify(a.read())
        file_b = binascii.unhexlify(b.read())

        xor_result = [hex(file_a[i]^file_b[i]) for i, byte in enumerate(file_a)]

    a.close()
    b.close()
   
    return ''.join(xor_result).replace('0x', '')


