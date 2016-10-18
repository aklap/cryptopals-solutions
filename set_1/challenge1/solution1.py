import base64
import binascii

def toBase64(hex_value):
    # decode input from hex to bytes
    binary_output = binascii.unhexlify(hex_value)
    
    # convert bytes to base64
    base64_output = base64.b64encode(binascii.unhexlify(hex_value))
    return base64_output.decode()
