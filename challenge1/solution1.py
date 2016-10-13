import base64
import binascii

def toBase64(hex_value):
    # decode input from hex to binary
    binary_output = binascii.unhexlify(hex_value)
    # convert binary to base64
    base64_output = base64.b64encode(binascii.unhexlify(hex_value))
    print(str(base64_output)[1:])

toBase64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
)