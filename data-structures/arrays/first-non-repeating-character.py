# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 23:14:34 2020

@author: Logan Rowe

Find the index of the first non-repeating character in a string

example strings:
    'aaabccc' --> b
    'aabbaazaa' --> z

only lowercase alphabetical characters no numbers or symbols.  

net coding time: 5 minutes
"""

def first_nonsequential_repeat_char(string):
    previous_letter=string[0]
    count=1
    for letter in string[0:]:
        if letter==previous_letter or (letter!=previous_letter and letter==string[count+1]):
            previous_letter=letter
            count+=1
        else:
            return(letter+' : '+str(count-1))

'''
A little more difficult:
    
    Find the first non-repeating character including all characters in the string.
    
example strings:
    'aaabcccdeeef' --> b
    'abcbad' --> c
    'abcabcabc' --> None
    
net coding time: 15 minutes
'''

#build a dictionary {'letter':# of appearances}
def first_non_repeat_char(string):
    letter_dict={}
    for letter in string:
        if letter not in letter_dict:
            letter_dict[letter]=1
        else:
            letter_dict[letter]+=1
    
    #Cycle through string once to find first occurence of non-repeating letter
    non_repeats=[letter for letter in letter_dict if letter_dict[letter]==1]
    for letter in string:
        if letter in non_repeats:
            return(letter+' : '+str(string.index(letter)))
            
if __name__ == '__main__':
    strings=['aaaajiiiidddduuuufgggjkk','aaabbbcccdeeed']
    for string in strings:
        print(first_nonsequential_repeat_char(string))
        print(first_non_repeat_char(string))
        print()