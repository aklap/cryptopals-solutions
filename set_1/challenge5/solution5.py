from xor import xor_encrypt


def get_xor_repeating(text, key):
    """XOR text with repeating crypto key."""
    return xor_encrypt(text, key)