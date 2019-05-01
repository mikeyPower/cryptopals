'''
Implement PKCS#7 padding
A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. But we almost never want to transform a single block; we encrypt irregularly-sized messages.

One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7.

So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. For instance,

"YELLOW SUBMARINE"
... padded to 20 bytes would be:

"YELLOW SUBMARINE\x04\x04\x04\x04"
'''

def main():
    text_to_pad = input("Enter text to pad : ")

    no_of_bytes = int(input("Enter Block Size : "))

    current_block_size = len(text_to_pad)

    if(current_block_size > no_of_bytes):
        print("Current string is larger than block size")
    elif (current_block_size == no_of_bytes):
        padding_bytes = no_of_bytes

    else:
        padding_bytes = no_of_bytes % current_block_size


    padding = str(hex(padding_bytes))
   # pad = padding.replace("0x","\\x0")
    for i in range(int(padding_bytes)):
        text_to_pad += padding

    print(text_to_pad)
if __name__== '__main__':
    main()
