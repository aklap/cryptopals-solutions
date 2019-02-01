def format_byte(byte):
    """Format the hex string."""
    # TODO: Is this necessary?
    if len(byte) < 4:
        return byte.replace('0x', '0')
    else:
        return byte[2:]


def to_string(text):
    """Join list as a string."""
    return ''.join(text)    
