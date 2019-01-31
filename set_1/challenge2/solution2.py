def get_XOR(file1, file2):
    """Given 2 strings, hex decode both and then XOR them, returning hex."""
    with open(file1) as a, open(file2) as b:

        a = bytes.fromhex(a.read())
        b = bytes.fromhex(b.read())
        # Use format specific mini language, 'x', to remove prefix
        # https: // docs.python.org/3/library/functions.html
        xor = ['%x' % (a[i] ^ b[i]) for i, byte in enumerate(a)]

        return ''.join(xor)
