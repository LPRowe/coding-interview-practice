# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:31:39 2020

@author: Logan Rowe

Given a string, find the shortest possible string which can be achieved by 
adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string st

A string consisting of lowercase English letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.

[output] string
"""

'''
Thoughts:
    
First I want to find the longest existing internal palendrome that ends at string[-1]
    i.e. for 'abcdc' --> 'cdc'
    
Second I want to append the reverse of the non-palendrome portion of the string
    i.d. 'abcdc' --> 'abcdc'+'ba'
    
'''

def isPalendrome(s):
    rev_s=s[::-1]
    half_length=int(len(s)/2)
    
    for (letter_forward,letter_backward) in zip(s[:half_length],rev_s[:half_length]):
        if letter_forward!=letter_backward:
            #mismatching letter found, s is not a palindrome
            return False
    
    #if it is a palendrome then
    return True

def buildPalendrome(s):
    #Check to see if s is already a palendrome
    if isPalendrome(s):
        return s
    
    #initially assume only the last letter in s is palendromic
    longest_palendrome=s[-1]
    
    #check to see if a longer palendrome exists within s, ending at s[-1]
    idx=1
    while idx<len(s)-1:
        if isPalendrome(s[idx:]):
            longest_palendrome=s[idx:]
            break
        idx+=1
    
    #use the index of the beginning of the longest internal palendrome to mirror
    #the letters at the beginning of s to the end of s
    s=s[:idx]+longest_palendrome+s[::-1][-idx:]
    
    return(s)
            
            
        
    
    
    

if __name__ == '__main__':
    s = "abcdc"
    print(buildPalendrome(s))