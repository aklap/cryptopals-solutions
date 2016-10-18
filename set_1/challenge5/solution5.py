from key import *
import binascii
from format import format_byte

def xor_encrypt(plaintext, key_string):
    key = Key(key_string)

    if type(plaintext) is str:
        plaintext = bytearray(plaintext, 'utf-8')
        return xor_repeat(plaintext, key, 'hex')
    else:
        return xor_repeat(plaintext, key, 'chr')

def xor_repeat(text, key, type):
    ciphertext = []

    for byte in text:
        key_char = key.chars[0]

        if type is 'hex':
            xbyte = hex(byte^ord(key_char))

        if type is 'chr':
            xbyte = chr(byte^ord(key_char))

        ciphertext.append(format_byte(xbyte))
        key.rotate()

    ciphertext_to_string = ''.join(ciphertext)    
    return ciphertext_to_string

