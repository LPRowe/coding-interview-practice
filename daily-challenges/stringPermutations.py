# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:33:03 2020

@author: Logan Rowe

Avoid using C++'s std::next_permutation or similar features in other languages 
to solve this challenge. Implement the algorithm yourself, since this is what 
you would be asked to do during a real interview.

Given a string s, find all its potential permutations. The output should be 
sorted in lexicographical order.

Example

For s = "CBA", the output should be
stringPermutations(s) = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"];
For s = "ABA", the output should be
stringPermutations(s) = ["AAB", "ABA", "BAA"].
Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string containing only capital letters.

Guaranteed constraints:
1 ≤ s.length ≤ 5.

[output] array.string

All permutations of s, sorted in lexicographical order.
"""

def stringPermutations(s):
    
    s=list(s)
    
    #Lock each letter in s at the front of the list
    for idx in range(len(s)):
        t=s[idx]+s[:idx]+s[idx+1:]
        
        #swap the second letter with all letters that come after it in s
        for idx2 in range(len(s)-1):
            t=t[:idx2]+t[idx2+1:]
        
        
if __name__=='__main__':
    stringPermutations('ABC')
    
    for permutation in stringPermutations('ABC'):
        print(permutation)