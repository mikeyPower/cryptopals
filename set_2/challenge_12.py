'''
An ECB/CBC detection oracle
Now that you have ECB and CBC working:

Write a function to generate a random AES key; that's just 16 random bytes.

Write a function that encrypts data under an unknown key --- that is, a function that generates a random key and encrypts under it.

The function should look like:

encryption_oracle(your-input)
=> [MEANINGLESS JIBBER JABBER]
Under the hood, have the function append 5-10 bytes (count chosen randomly) before the plaintext and 5-10 bytes after the plaintext.

Now, have the function choose to encrypt under ECB 1/2 the time, and under CBC the other half (just use random IVs each time for CBC). Use rand(2) to decide which to use.

Detect the block cipher mode the function is using each time. You should end up with a piece of code that, pointed at a block box that might be encrypting ECB or CBC,
tells you which one is happening.
'''
import base64
import random
import string
from Crypto.Cipher import AES


def ecb(key,message):
    #print("Using ecb encryption")
    #print(len(message))
    if(len(message)%16 != 0):
        i = 0
        zero = chr(0).encode('utf-8')
        length = len(message)
        while(i < 16-(length%16)):
            message+=zero
            i+=1
            #print(new_message)

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(message)
    return(encrypted)

def random_key_iv():
    key =""
    key_size = 16
    characters = string.digits + string.ascii_letters + string.punctuation
    for _ in range(key_size):
        key_char = random.choice(characters)
        key +=key_char

    return (key.encode("utf-8"))

def add_padding(message):
    number = random.randint(4, 10)
    add_byte = chr(number).encode('utf-8')
    return (add_byte*number+message+add_byte*number)

def base64_decode(message):
    decoded = base64.b64decode(message)
    return decoded #str(decoded, 'utf-8')


def determine_block_size():
    size = False
    count = 1
    first = 0
    text = b'a'

    while(size==False):
        key = random_key_iv()
        if(count == 1):
            first = len(ecb(key,text))
            count = count + 1

        elif(len(ecb(key,text)) > first):
            return(len(ecb(key,text))-first)

        else:
            text = text + b'a'









def main():

    unknown_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
    exit = 1
    decode_unknown_string = base64_decode(unknown_string)

    print("lenght of block cipher ",determine_block_size())

    while(exit > 0):
        key = random_key_iv()
        print(key)
        message = input("Enter message to be encrypted: ").encode("utf-8")
        #print(message)
        #print(decode_unknown_string)
        new_message = add_padding(message+decode_unknown_string)#.encode("utf-8")

        print(ecb(key,new_message))


        exit = int(input("Press 0 to exit else 1 to continue "))


if __name__== '__main__':
    main()
