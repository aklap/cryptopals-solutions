# KEYSIZE = 2..40

def get_hamming(a, b):
    a = bytearray(a, 'utf-8')
    b = bytearray(b, 'utf-8')
    count = 0
    # bytes
    for i, char in enumerate(a):
        a_bin = bin(char)[2:]
        b_bin = bin(b[i])[2:]
        pair = [a_bin, b_bin]
        difference = len(pair[1])-len(pair[0])

        if len(pair[0]) > len(pair[1]):
            pair.reverse()
            count += len(pair[1])-len(pair[0])
            # pair[1] = pair[1][:difference]
            print(pair[1])
            # count += compare(pair)

        if len(pair[0]) == len(pair[1]):
            count += compare(pair)

        # find the longer num
        # loop over that longer nums chars and compare ea char
    print(count)

def compare(pair):
    count = 0
    for i, digit in enumerate(pair[1]):
        if ord(digit) != ord(pair[0][i]):
            count+=1
    return count
get_hamming('this is a test', 'wokka wokka!!!')
