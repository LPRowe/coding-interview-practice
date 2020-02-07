# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 00:03:30 2020

@author: Logan Rowe

Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, 
return the number for which the second occurrence has a smaller index than the 
second occurrence of the other number does. If there are no such elements, return -1.

For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

net coding time: 5 minutes
"""

import numpy as np

def firstDuplicate(a):
    number_dictionary={}
    for number in a:
        if number not in number_dictionary:
            number_dictionary[number]=1
        elif number in number_dictionary:
            #first duplicate found
            return(number)
    #no duplicates found
    return(-1)
        
if __name__ == '__main__':
    a=np.array([2,1,3,5,3,2])
    print(firstDuplicate(a))