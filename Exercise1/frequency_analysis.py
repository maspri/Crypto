import numpy as np
import string

def replace_with(text,replacements):
    tmptext = text
    for a,b in replacements:
        tmptext = tmptext.replace(a.upper(),b)
    return tmptext

def calculate_frequency_table(text):
    freq_table = np.zeros(26)
    for char in cipher.lower():
        char = ord(char) - 97
        if char >= 0 and char < 26:
            freq_table[char]+=1
    return list(reversed(sorted(zip(freq_table,string.ascii_lowercase))))


f = open('01-2.txt','r')
cipher = f.read()
f.close()

freq_table = calculate_frequency_table(cipher)
print ("Frequency table for the cipher text:"+str(freq_table))

#key was determined by guessing the correct replacements, with help of the frequency table 
key = [('t','e'),('x','t'),('k','h'),('i','y'),('d','a'),('f','o'),('h','r'),('w','p'),('n','n'),('y','i'),('j','d'),('c','g'),('g','s'),('e','l'),('u','m'),('p','b'),('q','f'),('a','u'),('m','w'),('r','c'),('o','k'),('v','v'),('s','x'),('b','z')]
print("The key (determined by guessing the correct replacements, with help of the frequency table): \n"+str(key))


print ("The decypted text: \n"+str(replace_with(cipher,key)))

