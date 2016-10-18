from key import *
import binascii
from format import format_byte

def xor_encrypt(plaintext, string):
    key = Key(string)
    plaintext = bytearray(plaintext, 'utf-8')
    ciphertext = []

    for byte in plaintext:
        key_char = key.chars[0]
        xbyte = hex(byte^ord(key_char))
        ciphertext.append(format_byte(xbyte))
        key.rotate()

    ciphertext_to_string = ''.join(ciphertext)    
    return ciphertext_to_string

