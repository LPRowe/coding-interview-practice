# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:56:07 2020

@author: Logan Rowe

Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-1 ≤ a[i] ≤ 1000.

[output] array.integer

Sorted array a with all the trees untouched.
"""

def sortByHeight(a):
    #First let us figure out the best order for the people to stand in using a list
    b=[i for i in a if i!=-1]
    
    #let us sort b in reverse so we can use pop method when filling a
    b=sorted(b,reverse=True)
    
    #now lets us replace all people heights in a skipping over trees
    idx=0
    for i in a:
        if a[idx]==-1:
            idx+=1
        else:
            a[idx]=b.pop()
            idx+=1
            
    return(a)
    
if __name__=='__main__':
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    print(sortByHeight(a))