'''
Detect AES in ECB mode
In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
'''


import base64
from Crypto.Cipher import AES

def main():

    with open('7.txt') as fh:

        ciphertext = base64.b64decode(fh.read())

    print(ciphertext)
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)

if __name__ == "__main__":
    main()