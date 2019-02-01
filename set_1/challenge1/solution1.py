import base64

def toBase64(hex_string):
    """Take hexadecimal string and encode it as base64."""
    # Default encoding for .decode() is "utf-8"
    return base64.b64encode(bytes.fromhex(hex_string)).decode()
