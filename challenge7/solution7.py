import base64
from Crypto.Cipher import AES

# Well this was perfectly awful. I went to Python for crypto libs, and most all of crypto libraries are not for 3+. Had trouble installing via 2 different libs via pip for 3, and one required knowledge of a nonce/initialization vector, so ended up using 2.7 & pycrypto for this. 

with open('ciphertext.txt', 'rb') as f:
    while True:
        ciphertext = base64.b64decode(f.read()).rstrip()
        key = b'YELLOW SUBMARINE'
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = cipher.decrypt(ciphertext)

        print(plaintext)

        break
    f.close()
