'''
Implement CBC mode
CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block cipher natively only transforms individual blocks.

In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.

The first plaintext block, which has no associated previous ciphertext block, is added to a "fake 0th ciphertext block" called the initialization vector, or IV.

Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test),
and using your XOR function from the previous exercise to combine them.

The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)
'''
import base64
from Crypto.Cipher import AES

def test():
    obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
    message = b'The answer is no'
    ciphertext = obj.encrypt(message)
    print(ciphertext)
    obj2 = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
    print(obj2.decrypt(ciphertext))


def main():


    key = b'YELLOW SUBMARINE'
    # Create Initalization vector the lenght of the key used to encrypt the message
    iv=""
    for _ in range(len(key)):
        iv+="0"


    # Open the file
    with open('10.txt') as fh:

        #decode from ASCII to binary text format
        ciphertext = base64.b64decode(fh.read())
        #print(ciphertext)

    # Create a new cbc object based on the available parameters
    obj2 = AES.new(key, AES.MODE_CBC, iv.encode("utf-8"))

    # Decrypt cipher text
    print(obj2.decrypt(ciphertext))
    #test()

if __name__== '__main__':
    main()
