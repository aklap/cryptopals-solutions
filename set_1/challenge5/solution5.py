from key import *
import binascii

def encrypt(plaintext, string):
    key = Key(string)
    plaintext = bytearray(plaintext, 'utf-8')
    ciphertext = []

    for byte in plaintext:
        hexxed_xbyte = hex(byte^ord(key.chars[0]))
        if len(hexxed_xbyte) < 4:
            formatted_xbyte = hexxed_xbyte.replace('0x', '0')
        else:
            formatted_xbyte = hexxed_xbyte[2:]
        
        ciphertext.append(formatted_xbyte)
        key.rotate()

    ciphertext_to_string = ''.join(ciphertext)    
    return ciphertext_to_string

