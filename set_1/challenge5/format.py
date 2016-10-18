def format_byte(byte):
        if len(byte) < 4:
            return byte.replace('0x', '0')
        else:
            return byte[2:]