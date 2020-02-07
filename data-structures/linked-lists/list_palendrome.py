# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:33:52 2020

@author: Logan Rowe

Note: Try to solve this task in O(n) time using O(1) additional space, 
where n is the number of elements in l, since this is what you'll be asked to 
do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays 
just for simplicity of visualization: in real data you will be given a head 
node l of the linked list

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;

For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.
"""
import linked_lists_learning as lll

def isListPalindrome(l):
    #extract values from linked list
    values=[]
    current_node=l.head
    while current_node.next!=None:
        current_node=current_node.next
        values.append(current_node.data)
    
    for idx in range(int(len(values)/2)): #using int here will self hanlde the case that len(values is odd)
        if values[idx]!=values[-(idx+1)]:
            return False
    
    return True
    


    
    
if __name__=='__main__':
    l1=[0,1,0]
    l2=[1,2,2,3]
    
    link1=lll.linked_list()
    link2=lll.linked_list()
    for i in l1:
        link1.fastAppend(i)
        
    for i in l2:
        link2.fastAppend(i)
    
    print(link1.display())
    print(isListPalindrome(link1))
    print()
    print(link2.display())
    print(isListPalindrome(link2))
        