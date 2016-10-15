
from functools import reduce
import numpy as np

def break_xor(string1, string2):
    KEYSIZE = range(2,15)
    string1_bytes = bytearray(first_n, 'utf-8')
    string2_bytes = bytearray(second_n, 'utf-8')
    
    # normalized_distances = []
    # lowest = 100
    # key = 0

    # split byte array into chunks of KEYSIZE
    for n in KEYSIZE:
        first_chunks = getChunks(first_n, n)
        second_chunks = getChunks(second_n, n)
        distances = []
        print(f'For key {n}')

        for index, num in enumerate(first_chunks[0]):
            first_byte = num
            second_byte = second_chunks[0][index]
            # xor the bits in each byte, returning everthing after the binary prefix of 0b as a string
            xbyte = bin(first_byte ^ second_byte)[2:]   
            # count the differences by counting the occurrences of the 1 add onto count
            hamming_distance = xbyte.count('1')
            distances.append(hamming_distance)

        print(distances)
    #     # return an array of the normalized average hamming distance for each key
    #     normalized_distances.append(reduce(lambda a,b: a+b, distances)/n)
    #     print(normalized_distances)

    # # find the key which is the keysize with the lowest normalized hamming distance
    # for i, dist in enumerate(normalized_distances):
    #     if dist < lowest:
    #         key = KEYSIZE[i]
    #         lowest = dist
    # print(f'The keysize is {key}')
    
    # first_chunks = getChunks(first_n, key)
    # second_chunks = getChunks(second_n, key)
    # print(first_chunks, second_chunks)

    # prints 37 for hamming distance                
    # print(reduce(lambda a,b: a+b, hammings))

    #             if not lowest or avg < lowest[1]:
    #                 lowest = [n, avg]

    #     print(f'lowest keysize is {lowest}')
    #     print('--------------------------------\n')


    # chunks = getChunks(first_n, lowest[0])+ getChunks(second_n, lowest[0])
    # transposed = transpose(chunks)
    # print(f'XORed: {getXOR(transposed)}')

def hamming(string1, string2):
    distances = []
    for i, char in enumerate(string1):
                char_1 = char
                char_2 = string2[i]
                # xor the bits in each byte, returning everthing after the binary prefix of 0b as a string
                xbyte = bin(ord(char_1)^ord(char_2))
                # count the differences by counting the occurrences of the 1 add onto count
                hamming_distance = xbyte.count('1')
                distances.append(hamming_distance)
                
    return reduce(lambda a,b: a+b, distances)

# def hamming_average(hammings, n):
#     total = 0
#     for n in hammings:
#         total +=n
#     return total/n

# # method that takes bytes and returns n-sized bytes in a list structure
# def to_chunks(bytes, n):
#     start = 0
#     return [bytes[i:i + n] for i in range(0, len(bytes), n)]

# def transpose(chunks):
#     result0 = []
#     result1 = []
#     for i, chunk in enumerate(chunks):
#         result0.append(chunk[0])
#         result1.append(chunk[1])
#     return [result1, result0]

# def getXOR(transposed):
#     xbytes = []
#     for i, byte in enumerate(transposed[0]):
#         xbyte = bin(transposed[0][i] ^ transposed[1][i])
#         xbytes.append(xbyte)
#     return xbytes

