# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 01:45:23 2020

@author: Logan Rowe

A cryptarithm is a mathematical puzzle for which the goal is to find the 
correspondence between letters and digits, such that the given arithmetic 
equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing 
the mapping of letters and digits, solution. The array crypt will contain three 
non-empty strings that follow the structure: [word1, word2, word3], which should 
be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm 
with digits using the mapping in solution, becomes a valid arithmetic equation 
containing no numbers with leading zeroes, the answer is true. If it does not 
become a valid arithmetic solution, the answer is false.

Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

Example

For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be
isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, 
you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
the output should be
isCryptSolution(crypt, solution) = false.

Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, 
meaning that this is not a valid solution.
"""

'''
thoughts:
    
...I just spent 5 full minutes to understand what the problem is asking me to do :(

approach:

1) convert input words into numerical values based on the input solution
2) check to see if word1 + word2 = word3
3) invalidate result if any of the words have a leading zero
    
net coding time: 15 minutes
'''

def isCryptSolution(crypt, solution):
    #convert solution to a dictionary for ease of access
    solution=dict(solution)
    
    words=[]
    for word in crypt:
        encoded_word=''
        for letter in word:
            encoded_word+=solution[letter]
        words.append(encoded_word)
    
    #Check for leading zeroes to invalidate result
    for word in words:
        if word[0]=='0' and len(word)>1:
            return(False)
    
    #Check if the sum of numbers checks out
    if int(words[0])+int(words[1])!=int(words[2]):
        return(False)
    
    return(True)
    
        
    
    
    
    
    
    
if __name__ == '__main__':
    crypt1=["SEND", "MORE", "MONEY"]
    solution1=[['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
    
    crypt2=["TEN", "TWO", "ONE"]
    solution2=[['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
    
    print(isCryptSolution(crypt1,solution1))
    print()
    print(isCryptSolution(crypt2,solution2))