# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 00:57:59 2020

@author: Logan Rowe

Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a 
palindrome, false otherwise.
"""

'''
thoughts:
    
this one seems faily straight forward:

1) check each character to see if it occurs an even number of times
2) up to 1 character may occur an odd numer of times

'''

def palindromeRearranging(inputString):
    
    #track how many characters occur an odd number of times
    odd_char=0
    
    #track letters already checked
    letters=[]
    
    for letter in inputString:
        
        if letter in letters:
            continue
        
        if inputString.count(letter)%2==1:
            odd_char+=1
            letters.append(letter)
        else:
            letters.append(letter)
    
    if odd_char>1:
        return False
    else:
        return True