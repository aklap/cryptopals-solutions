
def get_hamming(first_n, second_n):
    KEYSIZE = range(2,15)
    first_n = bytearray(first_n, 'utf-8')
    second_n = bytearray(second_n, 'utf-8')
    distances = []
    lowest = []

    # split byte array into chunks of KEYSIZE
    for n in KEYSIZE:
        first_chunks = getChunks(first_n, n)
        second_chunks = getChunks(second_n, n)
        print(f'The key is {n}')
        
        for i, chunk in enumerate(first_chunks):
            hammings = []

            if i < 1:
                for index, num in enumerate(chunk):
                    first_byte = num
                    second_byte = second_chunks[i][index]
                    # xor the bits in each byte, returning everthing after the binary prefix of 0b as a string
                    xbyte = bin(first_byte ^ second_byte)[2:]
                    # count the differences by counting the occurrences of the 1 add onto count
                    hamming_distance = xbyte.count('1')
                    hammings.append(hamming_distance)
                avg = hamming_average(hammings, n)

                if not lowest or avg < lowest[1]:
                    lowest = [n, avg]

        print(f'lowest keysize is {lowest}')
        print('--------------------------------\n')


    chunks = getChunks(first_n, lowest[0])+ getChunks(second_n, lowest[0])
    transposed = transpose(chunks)
    print(f'XORed: {getXOR(transposed)}')


def hamming_average(hammings, n):
    total = 0
    for n in hammings:
        total +=n
    return total/n

def getChunks(bytes, n):
    start = 0
    return [bytes[i:i + n] for i in range(0, len(bytes), n)]

def transpose(chunks):
    result0 = []
    result1 = []
    for i, chunk in enumerate(chunks):
        result0.append(chunk[0])
        result1.append(chunk[1])
    return [result1, result0]

def getXOR(transposed):
    xbytes = []
    for i, byte in enumerate(transposed[0]):
        xbyte = bin(transposed[0][i] ^ transposed[1][i])
        xbytes.append(xbyte)
    return xbytes

get_hamming('this is a test', 'wokka wokka!!!')
