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

def mergeTwoLinkedLists(l1, l2):
    list1=[]
    list2=[]
    
    #Unpack linked lists into lists
    c=l1
    if c:
        list1.append(c.value)
    while c and c.next!=None:
        list1.append(c.next.value)
        c=c.next
    
    c=l2
    if c:
        list2.append(c.value)
    while c and c.next!=None:
        list2.append(c.next.value)
        c=c.next
    
    #dont bother sorting if there is only one list
    if len(list1)==0:
        return(list2)
    elif len(list2)==0:
        return(list1)
    
    sorted_list=[]
    while list1 and list2:
        #if both lists exist pick the lower value adn then remove it from that list
        if list1 and list2:
            sorted_list.append(np.min([list1[0],list2[0]]))
            if list1[0]==sorted_list[-1]:
                del list1[0]
            else:
                del list2[0]
        #once one list is completely empty just extend the sorted list by the remaining list
        if list1 and not list2:
            sorted_list.extend(list1)
            list1=[]
        if list2 and not list1:
            sorted_list.extend(list2)
            list2=[]

    return(sorted_list)