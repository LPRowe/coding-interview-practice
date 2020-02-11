# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:32:19 2020

@author: Logan Rowe

Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer
"""

def commonCharacterCount(s1, s2):
    '''
    keep track of how many characters are in both s1 and s2 where s1 and s2 are both strings
    
    ex: 
        s1='aabcc'
        s2='adcaa'
        
        commonCharacterCount(s1,s2)
        3
    '''
    
    #If either list has no length then return 0
    if len(s1)==0 or len(s2)==0:
        return 0
    
    common_character_counter=0
    
    #track of letters already accounted for
    letters=[]
    
    #For each letter that appears in s1 and s2 increase the common_character_count
    #by N where N is the smaller of how many times the letter appeared in s1 and s2
    for letter in s1:
        #increase count by the minimum number of times the letter occurs in either s1 or s2
        if (letter in s2) and (letter not in letters):
            common_character_counter+=min(s1.count(letter),s2.count(letter))
        letters.append(letter)

    return(common_character_counter)
    
    
if __name__=='__main__':
    s1='aabcc'
    s2='adcaa'
    print(commonCharacterCount(s1,s2))
    