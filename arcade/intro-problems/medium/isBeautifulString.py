# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:22:27 2020

@author: Logan Rowe

A string is said to be beautiful if each letter in the string appears at most
 as many times as the previous letter in the alphabet within the string; ie:
     b occurs no more times than a; c occurs no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be 
isBeautifulString(inputString) = true;

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f 
(and 0 of every other letter), so since there aren't any letters that appear 
more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be 
isBeautifulString(inputString) = false;

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be 
isBeautifulString(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there 
are no as, so therefore there are more bs than as.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ inputString.length ≤ 50.

[output] boolean

Return true if the string is beautiful, false otherwise.
"""

'''
thoughts...

this was a poorly phrased problem because it did not state wheter the alphabet
was a continuous loop.  i.e. whether 'aaz' is beautiful.

thought process is annotated within the function below
'''

import string

def isBeautifulString(inputString):
    #Use a dictionary to track how many times each letter is found in inputString
    letter_count={}
    for letter in string.ascii_lowercase:
        letter_count[letter]=0
                
    for letter in inputString:
        if letter_count[letter]==0:
            letter_count[letter]=inputString.count(letter)
    
    #Use another dictionary to see which letter precedes any given letter alphavetically
    alphabet=string.ascii_lowercase
    previous='z'+string.ascii_lowercase[:-1]
    previous_letter={alphabet[idx]:previous[idx] for idx in range(len(alphabet))}
    
    #check if the prevoius is in the word, it is in the word more times than the current letter    
    for letter in set(inputString):
        if letter_count[letter]>letter_count[previous_letter[letter]] and letter!='a':
            return False
    
    return True
    

if __name__=='__main__':
    inputStrings=["bbbaacdafe",'bbc']
    for s in inputStrings: print(isBeautifulString(s))
    
