# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 00:22:32 2020

@author: Logan Rowe

Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string picture

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

[output] array.string

The same matrix of characters, framed with a border of asterisks of width 1.
"""
import numpy as np
def addBorder_arr(picture):
    picture=np.array(picture)
    width=len(picture[0])
    height=len(picture)
    
    #let us make a new array that is the known size of the bordered picture
    #so as to conserve memory
    new_picture=np.full((height+2,width+2),'*')
    
    #Fill the inside with the original picture
    new_picture[1:-1,1:-1]=picture
    
    return(new_picture)
    
'''
We are given a list not a matrix so below is the solution used
to satisfy CodeSignal
'''

def addBorder(picture):
    width=len(picture[0])+2
    
    new_picture=['*'*width]
    for row in picture:
        new_picture.append('*'+row+'*')
    new_picture.append('*'*width)
    
    return(new_picture)
    
if __name__=='__main__':
    picture=['abc','def']
    
    for i in picture:
        print(i)

    print()
        
    for i in addBorder(picture):
        print(i)
