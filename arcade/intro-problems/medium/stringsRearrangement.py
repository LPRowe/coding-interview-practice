# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:39:18 2020

@author: Logan Rowe

Given an array of equal-length strings, you'd like to know if it's possible to 
rearrange the order of the elements in such a way that each consecutive pair 
of strings differ by exactly one character. Return true if it's possible, and 
false if not.

Note: You're only rearranging the order of the strings, not the order of the 
letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 
character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of 
strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), 
so return true.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string inputArray

A non-empty array of strings of lowercase letters.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 15.

[output] boolean

Return true if the strings can be reordered in such a way that each 
neighbouring pair of strings differ by exactly one character (false otherwise).
"""


'''
Thoughts:
    
1) create a dictionary for whree each string is a key and its value is 
    True if there is at least 1 other string with 1 or less character difference
2) If any string returns False then return False

'''
import numpy as np
from itertools import permutations


def stringsRearrangement(inputArray):
    inputArray=np.array(inputArray)
    
    #Build a dictionary consisting of all other strings within one permutation
    #i.e. {'abc':['abb','bbc','aac','abc',...]}
    string_dict={}
    
    #iterate through strings comparing each key string to all other strings
    for idx in range(len(inputArray)):
        key=inputArray[idx]
        string_dict[key]=[]
        for string in np.concatenate([inputArray[:idx],inputArray[idx+1:]]):
            
            #check to see if key is within one letter of the string
            count=np.sum([k!=s for (k,s) in zip(key,string)])
                    
            #do not add value to key if value==key or 2 or more letters are different
            if count>1 or count==0:
                continue
            else:
                #Add string to dictionary as a value if it is within 1 letter from the key
                string_dict[key]+=[string]    
    
    #from now on we do not need to compute whether string1 is within 1 letter change from 
    #string2 since it is stored in our dictionary
    
    #Given that there will be 10 strings or less in the given input array
    #it is not too expensive to check all possible permutations
    
    arr_len=len(inputArray)
    for permutation in list(permutations(range(arr_len))):

        #order inputArray values according to each permutation
        arr=inputArray[np.array(permutation)]
        
        #Count how many adjacent strings are more than 1 letter different
        discontinuities=np.sum([arr[idx+1] not in string_dict[arr[idx]] for idx in range(arr_len-1)])
       
        if discontinuities==0:
            #Made it to the end of the permutation and found no discontinuities. A solution exists!
            return True
        
    #Went through all permutations and all of them had at least one discontinuity.  No solution exists.
    return False
        
        
if __name__=="__main__":
    inputArrays=[["aba", "bbb", "bab"],["ab", "bb", "aa"],["ab", "ad", "ef", "eg"]]
    results=[False,True,False]
    for (inputArray,result) in zip(inputArrays,results):
        if stringsRearrangement(inputArray)==result:
            print("passed test")
        else:
            print('actual:',str(result))
        print()
