'''

Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
'''

import codecs

def generate_alphabet():
        alpha = []
        for i in range(26):
                alpha.append(chr(97+i))
        
        alpha.append('')
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
                if v > temp_v:
                        temp_v = v
                        temp_k = k
        return temp_k
def solve(cyrpt):
        # print(line.strip())
        cipher={}

        for i in range(256):

                hex_s = cyrpt.strip()

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
                cipher[sol.hex()]=key
            

        #print the highest value based on the largest key (which indicates the most frequest characters)        

        return highest_value(cipher)
def main():

    filename = "4.txt"
    result = []
    file = open(filename, "r")
    for line in file:
        result.append(solve(line))
            
    cipher = {}
    #print(result)
    for i in result:
        #print(i)
        freq = char_frequency(bytes.fromhex(i))
        key = sum_dict_values(freq)
       
        cipher[i]=key
        #print(key,bytes.fromhex(i))
    
    print(bytes.fromhex(highest_value(cipher)))
    


if __name__ == "__main__":
    main()