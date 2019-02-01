from key import Key
from format import *
import binascii

def xor_encrypt(text, key_string):
    """XOR encrypt plaintext with a given key."""
    # Initialize crypto key
    key = Key(key_string)
    # Convert plaintext to bytearray
    text = bytearray(text, 'utf-8')
    # Decrypt with key, rotating
    return xor_repeat(text, key)

def xor_repeat(bytes_text, key):
    """Repeat XOR decryption for text."""
    ciphertext = ''

    for byte in bytes_text:
        # Get first character in key string
        key_char = key.chars[0]
        xor_result = byte ^ ord(key_char)
        hex_str = hex(xor_result)
        # Append to previous encrypted bytes
        ciphertext += format_byte(hex_str)
        # Rotate the key
        key.rotate()

    return ciphertext
