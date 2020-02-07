# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:52:50 2020

@author: Logan Rowe

Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
"""


'''
thoughts:

we are provided with a list, but are supposed to be working with a linked list

I will create a linked list from the list but only include the values that
are not equal to given k

then I will return a list formed from the newly created linked list
'''
class ListNode(object):
   def __init__(self, data=None):
     self.data = data
     self.next = None
     
class LinkedList:
    def __init__(self):
        self.head=ListNode()

def removeKFromList(l,k):
    my_list=LinkedList()
    current_node=my_list.head
    for value in l:
        if value != k:
            current_node.next=ListNode(value)
            current_node=current_node.next
    
    new_list=[]
    current_node=my_list.head
    while current_node.next!=None:
        current_node=current_node.next
        new_list.append(current_node.data)
    return(new_list)
    

'''
If the input is in fact a linked list and not a list
props to metawrench for tips
'''

def removeKFromLinkedList(l,k):
    current_node=l
    while current_node:
        if current_node.next and current_node.next.data==k:
            current_node.next=current_node.next.next
        else:
            current_node=current_node.next
    return l.next if l and l.value==k else l            
    



if __name__=='__main__':
    l=[3, 1, 2, 3, 4, 5]
    k=3
    print(removeKFromList(l,k))
