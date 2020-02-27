# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:08:00 2020

@author: Logan Rowe

Given a string str and array of pairs that indicates which indices in the 
string can be swapped, return the lexicographically largest string that results 
from doing the allowed swaps. You can swap indices any number of times.

Example

For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
swapLexOrder(str, pairs) = "dbca".

By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", 
"dbca". The lexicographically largest string in this list is "dbca".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string str

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ str.length ≤ 104.

[input] array.array.integer pairs

An array containing pairs of indices that can be swapped in str (1-based). 
This means that for each pairs[i], you can swap elements in str that have the 
indices pairs[i][0] and pairs[i][1].

Guaranteed constraints:
0 ≤ pairs.length ≤ 5000,
pairs[i].length = 2.

[output] string
"""

'''
Start time: 12:08 am

Thoughts:
    
First I want a way to quantify which string is lexicographically longest
    
    1) create a dictionary linking each letter to a value {a:1, ... z:26}
    2) convert each string to a value like so to adc=1*100 + 4*10 + 3*1 (sort of like a hash)

Next, lets focus on each index 1 at a time

    1) what is the largest valued letter that can be swapped into index 1
    2) with this value fixed, what is the largest letter that can be swapped into index 2
    3)...this is starting to look like a problem that can be solved with recursion
    
As a stop statement in our recursion:
    
    1) If len(remaining_string)==1 return remaining_string
    
    
12:20 am... rethinking this approach

Since different permutations of the pairs will result in different outcomes
the brute force method would be to test all permutations as well as incomplete
permutations...

Instead, I see that in the example 'd' can go to position 1 because position 3 is
connected to position 4 ([3,4]) and position 4 is connetect to position 1 ([1,4])

I will make a map of all the values each letter can connect to and use that to build
our "largest value" word
'''

import string
from itertools import permutations
lex_values={*zip(string.ascii_lowercase,[i for i in range(26)])}

#build a dictionary showing all locations a value starting at index i could go to
index_map={}
idx=0
for pair in pairs:
    for val in pair:
        for pair in pairs[:idx]+pairs[idx+1:]:
            if val in pair:
                if val in index_map.keys():
                    index_map[val]=index_map[val].add(i for i in pair if i!=val)
                else:
                    index_map[val]=set(i for i in pair if i!=val)
                

def swapLexOrder(word,pairs):
    global lex_values
    
    #build  a map of indices where each letter could go
    letter_location_map={}
    for letter in word:
        letter_idx=word.index(letter)+1 #plus 1 because the given pair [1,4] actually refers to indices [0,3]
        for pair in pairs:
            if letter_idx in pair:
                if letter in letter_location_map.keys():
                    letter_location_map[letter]=letter_location_map[letter].add(i for i in pair if i!=letter_idx)
                else:
                    letter_location_map[letter]=set(i for i in pair if i!=letter_idx)
                
                #continue building the chain
                for idx in letter_location_map[letter]:
                    
        print(letter_location_map)
            
    
    
    
    
    
if __name__=='__main__':
    s='abdc'
    pairs=[[1,4],[3,4]]
    swapLexOrder(s,pairs)