import numpy as np
import string,re

def decrypt(text,key):
    decrypted = ""
    i = 0
    n = len(key)
    for char in text.lower():
        charn = ord(char) - 97
        if charn >= 0 and charn < 26:
            charn = (charn - (ord(key[i])-97)) % 26
            decrypted = decrypted + str(chr(charn+97))
            i = (i + 1) %  n
        else:
            decrypted = decrypted + str(char)
    return decrypted
            

def freq_table(text,K,offset=0):
    '''
    Input:
        text:  string - cipher text
        K = numpy array - natural numbers
    Returns:
    frequency table
    '''
    #remove non letters from the text
    text = re.sub('[^a-zA-Z]','',text)
    freq_table = np.zeros((K.size,26))
    for i,k in enumerate(K):
        num_letters = 0
        for char in text[offset::k].lower():
            char = ord(char) - 97
            if char >= 0 and char < 26:
                num_letters+=1
                freq_table[i,char]+=1
        
        freq_table[i,:] = freq_table[i,:] / float(num_letters)
        
    return freq_table

def find_letters(text,key_len,target_frequencies):
    
    most_probable_keyletters = np.zeros((key_len,26),dtype=np.int32)
    
    for a in range(key_len):
        frequency_table = freq_table(text,np.array([key_len]),a)
        
        sums = np.zeros(26)
        for shift in range(26):
            sums[shift] = np.sum(np.dot(np.roll(frequency_table,-shift),target_frequencies/100))
        most_probable_keyletters[a,:] = np.argsort(np.abs(sums-0.065))
        
        
    return most_probable_keyletters

english_freq = np.array([8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,
                0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,
                6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074])

f = open('02-1.txt','r')
cipher = f.read()
f.close()

frequencies = freq_table(cipher,np.array(range(1,11)))
sums = np.sum(frequencies**2,axis=1)
key_len = np.argmin(np.abs(sums-0.065))+1

print ("The keyword length is probably: "+str(key_len))

most_probable_keyletters = find_letters(cipher,key_len,english_freq)

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i,letters in enumerate(most_probable_keyletters):
    print ("Most probable letters for "+str(i)+"'th letter:",flush=True)
    for char in letters:
        print (str(alphabet[char])+" ",end="",flush=True)
    print('')

decr = decrypt(cipher,"geheim")

print("The decrypted text is:\n"+decr)

