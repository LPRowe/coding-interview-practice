# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:23:10 2020

@author: Logan Rowe

Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint 
substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a 
concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order 
and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

String consisting of lowercase English letters.

Guaranteed constraints:
4 ≤ s.length ≤ 15.

[output] string

Encoded version of s.
"""

def lineEncoding(s):
    split_letters=''
    
    prev_letter=s[0]
    for letter in s:
        if letter==prev_letter:
            split_letters+=letter
        else:
            split_letters+=','+letter
            prev_letter=letter
            
    encoded_list=[str(len(i))+i[0] for i in split_letters.split(',')]
    
    idx=0
    for i in encoded_list:
        if i[0]=='1' and len(i)==2:
            encoded_list[idx]=i[1]
        idx+=1
            
    encoded_string=''.join(encoded_list)
    
    return(encoded_string)
    
    
    
if __name__=='__main__':
    strings = ["aabbbc",'ccccccccccccccc']
    for s in strings:
        print(lineEncoding(s))