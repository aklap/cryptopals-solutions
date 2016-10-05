import base64

def toBase64(hex_string):
    bytes = bytearray.fromhex(hex_string)
    # This returns a byte object, and thus is prefixed with a 'b'; the comparison will thus fail because it is not a string; hence, the decode call added below. 
    converted_base64 = base64.b64encode(bytes).decode('utf-8')

    if converted_base64 == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t':
        print(f"Converted to: {converted_base64}")

toBase64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
)