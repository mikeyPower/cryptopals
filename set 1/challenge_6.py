'''
Break repeating-key XOR
It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
this is a test
and
wokka wokka!!!
is 37. Make sure your code agrees before you proceed.
For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
Solve each block as if it was single-character XOR. You already have code to do this.
For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.

No, that's not a mistake.
We get more tech support questions for this challenge than any of the other ones. We promise, there aren't any blatant errors in this text. In particular: the "wokka wokka!!!" edit distance really is 37.
'''


def hamming_distance(string1,string2):
    bin1 = string_to_binary(string1)
    bin2 = string_to_binary(string2)

    #bin1 = bin1[2:]
    #bin2 = bin2[2:]

    dif = 0
    print(len(bin1))
    print(len(bin2))
    if len(bin1)>len(bin2):
        dif = len(bin1)-len(bin2)
        for i in range(dif):
            bin2='0'+bin2

        #print(bin2)
    elif len(bin2)>len(bin1):
        dif = len(bin2)-len(bin1)
        for i in range(dif):
            bin1='0'+bin1
        #print(bin1)
    else:
        dif =0

    #print(len(bin1))
    #print(len(bin2))

    dif = 0
    for i in range(len(bin1)):
        print(bin1[i],bin2[i])
        if(bin1[i]!=bin2[i]):
            #print(bin1[i],bin2[i])
            dif+=1


    return dif


    
def string_to_binary(string1):

    return ''.join(format(ord(x), 'b') for x in string1)



def get_binary_value(string1):
    total=''
    for i in range(len(string1)):
        total=bin(ord(string1[i]))[2:]+total
    #print(total)
    return total

def main():
    string1 = "this is a test"
    string2 = "wokka wokka!!!"
    print(string_to_binary(string1))
    print(string_to_binary(string2))
    print(hamming_distance(string1,string2))

if __name__ == "__main__":
    main()