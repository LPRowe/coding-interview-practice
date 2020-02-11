# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 23:05:13 2020

@author: Logan Rowe

Write a function that reverses characters in (possibly nested) parentheses 
in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters and the characters ( and ). 
It is guaranteed that all parentheses in inputString form a regular bracket sequence.

Guaranteed constraints:
0 ≤ inputString.length ≤ 50.

[output] string

Return inputString, with all the characters that were in parentheses reversed.
"""

'''
I will try to include my thought process on any coding challenge that I do not
feel a good approach is rather clear

Thoughts:

I want to work from the inside to the outside.  And will want to use a mutable
datatype to swap the order of letters as opposed to an immutable string.  

1) convert the string to an array of length len(string))
2) reverse the inner most parentheses first
3) replace the parentheses with a free symbol ($) so as not to change array size
4) repeat until there are no more parenthesis
5) remove free symbols ($) while converting the array to a string

'''

import numpy as np

def reverseInParentheses(inputString):
    arr_input=np.array([letter for letter in inputString])
    
    #repeatedly flip inner most parenthesis and replace parens until there
    #are no more parentheses sections to flip
    while '(' in arr_input:
        idx=0
        #Find the indices of the inner most parenthesis
        #when we hit break it should be '('+letters+')' since the idx for '('
        #is continuously updated
        for letter in arr_input:
            if letter=='(':
                left_idx=idx
            if letter==')':
                right_idx=idx
                break
            idx+=1

        
        #Reverse the section between parenthesis
        between_paren=arr_input[left_idx+1:right_idx]
        reverse=[letter for letter in reversed(between_paren.tolist())]
        
        #replace the forward section with the reverse section
        arr_input[left_idx+1:right_idx]=reverse
        
        #Replace them with a free symbol
        arr_input[right_idx]='$'
        arr_input[left_idx]='$'
    
    #Remove all free symobls ($)
    arr_input=[letter for letter in arr_input if letter!='$']
    
    #Now convert array back to string
    outputString=''.join(arr_input)
    
    return(outputString)

if __name__=='__main__':
    '''
    Lets set up some simple tests for this one to speed up the debugging process
    '''
    
    inputs=["(bar)","foo(bar)baz","foo(bar)baz(blim)","foo(bar(baz))blim",]
    outputs=['rab',"foorabbaz","foorabbazmilb","foobazrabblim"]
    
    for (i,j) in zip(inputs,outputs):
        if reverseInParentheses(i)==j:
            print('Passed Inspection')
        else:
            print('\nFail:\n',reverseInParentheses(i),'is not',j,'\n')
            