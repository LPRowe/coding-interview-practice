# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:24:37 2020

@author: Logan Rowe

You're given 2 huge integers represented by linked lists. Each linked list 
element is a number from 0 to 9999 that represents a number with exactly 4 digits. 
The represented number might have leading zeros. Your task is to add up these 
huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.
"""

# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def addTwoHugeNumbers(a, b):
    a_string=''
    b_string=''
    lz='0000' #leading zeroes

    len_a=0
    len_b=0

    current_node=a
    a_string+=str(current_node.value)
    while current_node and current_node.next!=None:
        current_node=current_node.next

        #If the nubmer is shorter than 4 digits add leading zeroes
        if len(str(current_node.value))<4:
            string=lz[:-1*len(str(current_node.value))]+str(current_node.value)
        else:
            string=str(current_node.value)

        #Extend string with updated current_node value
        a_string+=string
        len_a+=1
    
    print(a_string)

    current_node=b
    b_string+=str(current_node.value)
    while current_node and current_node.next!=None:
        current_node=current_node.next

        #If the nubmer is shorter than 4 digits add leading zeroes
        if len(str(current_node.value))<4:
            string=lz[:-1*len(str(current_node.value))]+str(current_node.value)
        else:
            string=str(current_node.value)

        #Extend string with updated current_node value
        b_string+=string
        len_b+=1

    print(b_string)

    #If null lists then return [0]
    N=max([len_a,len_b])
    if N==0:
        return([0])

    summation=int(a_string)+int(b_string)
    summation=str(summation)

    print(summation)

    #Add leading Zeroes back into summation and then full string into groups of 4
    remainder=len(summation)%4
    if remainder!=0:
        summation='0'*(4-remainder)+summation

    strings=[]
    for s in range(int(len(summation)/4)):
        strings.append(summation[s*4:(s+1)*4])
    
    c=ListNode(int(strings[0]))
    while c and c.next!=None:
        for s in strings[1:]:
            c=c.next
            c=ListNode(int(s))

    strings=[int(s) for s in strings]
    print(strings)

    return strings