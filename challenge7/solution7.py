import base64
from Crypto.Cipher import AES

with open('ciphertext.txt', 'rb') as f:
    while True:
        ciphertext = base64.b64decode(f.read()).rstrip()
        key = b'YELLOW SUBMARINE'
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = cipher.decrypt(ciphertext)

        print(plaintext.decode('ascii'))

        break
    f.close()
