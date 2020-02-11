# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:41:53 2020

@author: Logan Rowe

Followed a tutorial to learn the basic functions such as append, length, display
and get

Then challenged myself to improve on the list structure by adding functions such
as fastAppend which is O(1) instead of O(n) and insert
"""

import numpy as np

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()
        self.tail=self.head
        
    def append(self,data):
        new_node = node(data)
        current_node=self.head
        while current_node.next!=None:
            current_node=current_node.next
        current_node.next=new_node
        self.tail=new_node
        
    def fastAppend(self,data):
        new_node=node(data)
        self.tail.next=new_node
        self.tail=new_node
        

    def length(self,start_node=None):
        '''
        Measure the length of the linked list starting at the head node
        
        if start_node=node then linked list will be measured from that node to the end
        '''
        idx=0
        if start_node:
            current_node=start_node
        else:
            current_node=self.head
            
        while current_node!=None:
            idx+=1
            current_node=current_node.next
        return(idx)
        
    def display(self):
        '''
        display the current contents of the list
        '''
        elems = []
        current_node=self.head
        while current_node:
            elems.append(current_node.data)
            current_node=current_node.next
        if None in elems:
            elems.remove(None)
        return(elems)
    
    def get(self,index):
        '''
        return the data point at a given index
        '''
        L=self.length()
        if index>=L:
            print("Requested index is out of range.\nMax range is:",str(L))
            return(None)
            
        idx=0
        current_node=self.head
        while True:
            current_node=current_node.next
            if idx==index: 
                return(current_node.data)
            idx+=1
            
    def erase(self,index):
        '''
        remove the node at given index from list
        '''
        idx=0
        current_node=self.head
        while idx<index:
            current_node=current_node.next
            idx+=1
            
        #change connection to skip the node to be erased    
        current_node.next=current_node.next.next
        
    def insert(self,data,index):
        '''
        Insert a new node into the list at given index with given data value
        '''
        new_node=node(data)
        
        idx=0
        current_node=self.head
        while idx<index:
            current_node=current_node.next
            idx+=1
        
        new_node.next=current_node.next
        current_node.next=new_node
    
    def reverse(self):
        '''
        reverse the entire linked list
        '''
        previous=None
        current_node=self.head
        while current_node!=None:
            #retain next node as future
            future=current_node.next
            
            #make current node point back to previous node
            current_node.next=previous
            
            #retain current node as new previous node
            previous=current_node
            
            #Change current node to future
            current_node=future
        
        
        self.tail=self.head
        self.head=previous
        
    net_count=0        
    def reverseBatches(self,head,k,net_count=net_count):
        previous=None
        future=None
        current_node=head
        count=0
        
        ll_len=self.length(start_node=current_node)
        #print(ll_len)
        
        if ll_len>=k:
            modulo=k
        else:
            modulo=1
            
        while current_node!=None and count<modulo:
            #retain next node as future
            future=current_node.next
            
            #make current node point back to previous node
            current_node.next=previous
            
            #retain current node as new previous node
            previous=current_node
            
            #Change current node to future
            current_node=future
            
            count+=1
            

            
        if future!=None:
            head.next=self.reverseBatches(future,k)
        
        return(previous)
            
        
        
        self.tail=self.head
        self.head=previous
    
    def reverse2(self, head, k): 
        current = head  
        next  = None
        prev = None
        count = 0 
          
        # Reverse first k nodes of the linked list 
        while(current is not None and count < k): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next 
            count += 1
  
        # next is now a pointer to (k+1)th node 
        # recursively call for the list starting 
        # from current. And make rest of the list as 
        # next of first node 
        if next is not None: 
            head.next = self.reverse2(next, k) 
  
        # prev is new head of the input list 
        return prev 
        
        
        
            
            
        

if __name__ == '__main__':
    my_list=linked_list()
    for i in [1,2,3,4,5,6,7,8,9,10,11]:
        my_list.fastAppend(i)
    
    #print(my_list.display())
    
    print(my_list.display())
    my_list.head=my_list.reverseBatches(my_list.head.next,3)
    print(my_list.display())

        
