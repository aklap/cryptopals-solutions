import sys

def getXOR(file1, file2):

    with open(str(file1), "rb") as a, open(str(file2), "rb") as b:
        xor_result = [];

        while True:
            abyte = a.read(1)
            bbyte = b.read(1)

            if toDecimal(abyte) != 'empty':
                xbyte = toDecimal(abyte)^toDecimal(bbyte)
                res_byte = format(xbyte, 'x')
                xor_result.append(res_byte)

            if not abyte:
                break

        print("The XOR result is:", "".join(xor_result))

    a.close()
    b.close()

def toDecimal(hex):
    if hex.decode('ascii') == "":
        return 'empty'
    else:
        return int(hex, 16)

getXOR("./buffer1.txt", "./buffer2.txt")
