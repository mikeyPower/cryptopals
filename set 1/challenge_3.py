'''

Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
'''

import codecs

def generate_alphabet():
        alpha = []
        for i in range(26):
                alpha.append(chr(97+i))
        
        return alpha

def inti_dict():
        char_dict = {}
        alph = generate_alphabet()
        for i in alph:
                
                char_dict[i]=0
        return char_dict
                
def char_frequency(message):
        alph = generate_alphabet()
        char_dict = dict(inti_dict())
      
        for i in message:
                
                if chr(i) in alph:
                        char_dict[chr(i)]+=1
        return char_dict
def sum_dict_values(dict_v):
        total = 0
        for k,v in dict_v.items():
                total+=v
        return total

def fix_xor(plain, k):
        cipher = bytearray()
        for i in range(len(plain)):
            cipher.append(plain[i]^ k)
        return cipher

def highest_value(dict_v):
       
        temp_k = next(iter(dict_v))
        temp_v = dict_v[temp_k]
        for k,v in dict_v.items():
                if k > temp_k:
                        temp_v = v
                        temp_k = k
        return temp_v

def main():
        cipher={}
        for i in range(256):

                hex_s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

                #convert hex to ascii
                barray = codecs.decode(hex_s,'hex')

                #xor ascii string with each character value
                sol =  fix_xor(barray,i)

                #get a frequency of each character as a dict with the letter as key and number of times
                #they appear as a value in the xor result
                freq = char_frequency(sol)

                #sum all dict values for that result
                key = sum_dict_values(freq)

                #store the values as the key and the xor result as the value
                cipher[key]=sol
        

        #print the highest value based on the largest key (which indicates the most frequest characters)        
        print(highest_value(cipher))
        




if __name__ == "__main__":
    main()