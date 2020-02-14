# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:10:19 2020

@author: Logan Rowe

Given an array of integers nums and an integer k, determine whether there are 
two distinct indices i and j in the array where nums[i] = nums[j] and the 
absolute difference between i and j is less than or equal to k.

Example

For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
containsCloseNums(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions is exactly 3.

For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
containsCloseNums(nums, k) = false.

The absolute difference between the positions of the two 2s is 3, which is more than k.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

Guaranteed constraints:
0 ≤ nums.length ≤ 55000,
-231 - 1 ≤ nums[i] ≤ 231 - 1.

[input] integer k

Guaranteed constraints:
0 ≤ k ≤ 35000.

[output] boolean
"""

'''
convert nums to a dictionary where d={number:[indices],number2:[indices],...}
'''

def absDiff(int_list):
    absDiff=[]
    for index in range(len(int_list)):
        start=int_list[index]
        end=int_list[:index]+int_list[index+1:]
        for value in end:
            absDiff.append(abs(start-value))
    
    return(min(absDiff))

def containsCloseNums(nums, k):
    
    num_dict={num:[] for num in nums}
    
    index=0
    for num in nums:
        num_dict[num].append(index)
        index+=1
    
    #iterate throug heach key in the dictionary
    for num in num_dict:
        #if there was more than one occurence of the number check the distance between indices
        if len(num_dict[num])>1:
            if absDiff(num_dict[num])<=k:
                return True
    return False
        
    
    
    
if __name__=='__main__':
    nums = [[0, 1, 2, 3, 5, 2], [0, 1, 2, 3, 5, 2]]
    ks=[3,2]
    for (num,k) in zip(nums,ks):
        print(containsCloseNums(num,k))
        
    int_list=[1,2,3]
    print(absDiff(int_list))
    