# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:20:02 2020

@author: Logan Rowe

Given a sequence of integers as an array, determine whether it is possible to 
obtain a strictly increasing sequence by removing no more than one element 
from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if 
a0 < a1 < ... < an. Sequence containing only one element is also considered 
to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a 
strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. 
Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to 
get a strictly increasing sequence, otherwise return false.
"""

def almostIncreasingSequence(seq):
    # =============================================================================
    # Check to see if the sequence is already monotonically increasing
    # =============================================================================
    idx=0 #idx lags one behind the index of the squence
    for i in seq[1:]:
        if i<=seq[idx]:
            # =============================================================================
            # If it is not monotonically increasing create two new lists
            # where each list represents one possible solution
            # =============================================================================
            s1=[i for (i,loc) in zip(seq,range(len(seq))) if loc!=idx]
            s2=[i for (i,loc) in zip(seq,range(len(seq))) if loc!=idx+1]
            print(s1)
            print(s2)
        idx+=1
        
    passing_seq=0
    
    
    # =============================================================================
    # Check both new lists to see if either is increasing monotonically
    # =============================================================================
    idx=0
    if s1:
        for i in s1[1:]:
            if i<=s1[idx]:
                passing_seq-=1
                break
            idx+=1
        passing_seq+=1
    
    idx=0
    if s2:
        for i in s2[1:]:
            if i<=s2[idx]:
                passing_seq-=1
                break
            idx+=1
        passing_seq+=1
    
    # =============================================================================
    # if either s1 or s2 is increasing monotonically then passing_seq will be 1 or greater
    # =============================================================================
    if passing_seq>=1:
        return True
    else:
        return False
    

if __name__=='__main__':
    List=[1,2,1,2]
    print(almostIncreasingSequence(List))