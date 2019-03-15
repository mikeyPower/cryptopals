'''
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179
'''

import codecs

def fix_xor(plain, k):
        cipher = bytearray()
        for i in range(len(plain)):
            cipher.append(plain[i]^k[i])
        return cipher

def main():

    barray1 = codecs.decode('1c0111001f010100061a024b53535009181c','hex')
    barray2 = codecs.decode('686974207468652062756c6c277320657965','hex')

    xor = fix_xor(barray1,barray2)
    
    print(xor)
    print(codecs.encode(xor,'hex'))

    # check the answer
    assert(xor == codecs.decode('746865206b696420646f6e277420706c6179','hex'))

if __name__ == "__main__":
    main()