from key import *
import binascii

def decode(plaintext, string):
    expected = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    key = Key(string)
    plaintext = bytearray(plaintext, 'utf-8')
    ciphertext = []

    for byte in plaintext:
        xbyte = byte ^ ord(key.chars[0])
        if len(xbyte) < 4:
            formatted_xbyte = hex(xbyte).replace('0x', '0')
        else:
            formatted_xbyte = hex(xbyte)[2:]
        
        ciphertext.append(formatted_xbyte)
        key.rotate()

    print(''.join(ciphertext) == expected)

decode("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", 'ICE')