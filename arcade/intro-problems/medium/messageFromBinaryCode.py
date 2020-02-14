# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:39:07 2020

@author: Logan Rowe

You are taking part in an Escape Room challenge designed specifically for 
programmers. In your efforts to find a clue, you've found a binary code written 
on the wall behind a vase, and realized that it must be an encrypted message. 
After some thought, your first guess is that each consecutive 8 bits of the 
code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.

Example

For code = "010010000110010101101100011011000110111100100001", the output should be
messageFromBinaryCode(code) = "Hello!".

The first 8 characters of the code are 01001000, which is 72 in the binary 
numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
Other letters can be obtained in the same manner.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string code

A string, the encrypted message consisting of characters '0' and '1'.

Guaranteed constraints:
0 < code.length < 800.

[output] string

The decrypted message.
"""


def messageFromBinaryCode(code):
    elements=[int(code[index*8:(index+1)*8],2) for index in range(int(len(code)/8))]
    elements=[chr(element) for element in elements]
    return(''.join(elements))
    
    
    
if __name__=='__main__':
    code = "010010000110010101101100011011000110111100100001"
    print(messageFromBinaryCode(code))