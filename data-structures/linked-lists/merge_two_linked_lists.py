# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:58:48 2020

@author: Logan Rowe

Note: Your solution should have O(l1.length + l2.length) time complexity, 
since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, 
your task is to merge them. In other words, return a singly linked list, also 
sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
"""

import numpy as np

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def mergeTwoLinkedLists(l1, l2):
    sorted_list=ListNode(None)
    curr=sorted_list
    while l1 and l2:
        if l1.value <= l2.value:
            curr.next=l1
            l1=l1.next
        else:
            curr.next=l2
            l2=l2.next
        curr=curr.next
        
    #once one of the lists is depleted we will break out of while loop
    #Take all remaining values from whichever list remains
    while l1:
        curr.next=l1
        l1=l1.next
    while l2:
        curr.next=l2
        l2=l2.next

    return(sorted_list.next)