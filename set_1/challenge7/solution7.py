import base64
from Crypto.Cipher import AES

def decrypt_AES():
    plaintext = ""

    with open('ciphertext.txt', 'rb') as f:
        while True:
            ciphertext = base64.b64decode(f.read()).rstrip()
            key = b'YELLOW SUBMARINE'
            cipher = AES.new(key, AES.MODE_ECB)
            plaintext_bytes = cipher.decrypt(ciphertext)
            plaintext = plaintext_bytes.decode()
            break
        f.close()

    return plaintext

