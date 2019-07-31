cle'''
Detect AES in ECB mode
In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
'''
#Not Completed

import base64
from Crypto.Cipher import AES

def main():
    for i in open('8.txt','rb'):
        #print(i)
        ciphertext =[i.strip().decode('utf-8')]

    bsize = 16



    print(ciphertext)
   # print(len(ciphertext))


    block = [ciphertext[i:i+bsize] for i in range(0, len(ciphertext), bsize)]
    print(type(block))
    no_repeat = len(block) - len(set(block))
    result = {
      'ciphertext': ciphertext,
      'repetitions': no_repeat
    }

    repeating = [result for cipher in ciphertext]


    most_repeating = sorted(repeating, key=lambda x: x['repetitions'], reverse=True)[0]
   # key = b'YELLOW SUBMARINE'
   # cipher = AES.new(key, AES.MODE_ECB)
   # plaintext = cipher.decrypt(ciphertext[0])
    print("Ciphertext: {}".format(most_repeating['ciphertext']))
    print("Repeating Blocks: {}".format(most_repeating['repetitions']))
   # print(plaintext)

if __name__ == "__main__":
    main()
