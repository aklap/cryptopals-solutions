from functools import reduce

def normalize(pair, k):
    distance = hamming(pair[0].decode(), pair[1].decode())
    return distance/k

def hamming(string1, string2):
    distances = []

    for i, char in enumerate(string1):
        xbyte = bin(ord(char)^ord(string2[i]))
        distances.append(xbyte.count('1'))
    return (reduce(lambda a,b: a+b, distances))
