# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:12:12 2020

@author: Logan Rowe

Define a word as a sequence of consecutive English letters. 
Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string text

Guaranteed constraints:
4 ≤ text.length ≤ 50.

[output] string

The longest word from text. It's guaranteed that there is a unique output.
"""

import string

def longestWord(text):
    letters=string.ascii_letters
    
    words=''
    for letter in text:
        if letter in letters:
            words+=letter
        else:
            words+=','
    
    longest_word=max(words.split(','),key=len)
    return(longest_word)
    
    

if __name__=='__main__':
    s="You are the best!!!!!!!!!!!! CodeFighter ever!"
    print(longestWord(s))