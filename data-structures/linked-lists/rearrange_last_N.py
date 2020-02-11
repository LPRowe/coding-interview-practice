# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:53:06 2020

@author: Logan Rowe

Note: Try to solve this task in O(list size) time using O(1) additional space,
since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, 
move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer n

A non-negative integer.

Guaranteed constraints:
0 ≤ n ≤ list size.

[output] linkedlist.integer

Return l with the n last elements moved to the beginning.
"""

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def rearrangeLastN(l, n):
    #Edge Case if n is <=0 just return the original linked list
    if n<=0:
        return l

    #Find the length of the list
    ll_len=0
    head=l
    curr=head
    while curr!=None:
        ll_len+=1
        curr=curr.next
    
    #Edge Cases: If len(l)==0 or len(l)>=n return the original linked list
    if ll_len<=n or ll_len==0:
        return l

    #Edge Case: If len(l) is 2 then reverse the list and return
    if ll_len==2:
        head=l
        curr=head
        prev=curr
        new_head=curr.next
        new_head.next=prev
        prev.next=None
        return(new_head)

    #make new_head in the list at ll_len-n and old tail point to old head 
    index=0
    old_head=l
    curr=old_head
    while curr and curr.next!=None:
        curr=curr.next
        index+=1

        if index==ll_len-n:
            new_head=curr

        if index==ll_len-n-1:
            new_tail=curr
    
    #After passing to the last item in the list, point it towards the original head
    curr.next=old_head

    new_tail.next=None

    l=new_head

    return(l)
    
if __name__=='__main__':
    l = [1, 2, 3, 4, 5]
    head=ListNode(None)
    curr=head
    for value in l:
        curr.next=ListNode(value)
        curr=curr.next
        print(value)
    
    print()
        
    rearranged_ll=rearrangeLastN(head.next,3)
    curr=rearranged_ll
    while curr!=None:
        print(curr.value)
        curr=curr.next    