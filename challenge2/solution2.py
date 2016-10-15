import sys

def getXOR(file1, file2):

    with open(str(file1), "rb") as a, open(str(file2), "rb") as b:
        xor_result = [];

        while True:
            a_byte = a.read(1)
            b_byte = b.read(1)

            if a_byte.decode('ascii') != '':
                xbyte = ord(a_byte)^ord(b_byte)
                res_byte = format(xbyte, 'x')
                xor_result.append(res_byte)

            if not a_byte:
                break
    a.close()
    b.close()
   
    print("The XOR result is:", "".join(xor_result))

