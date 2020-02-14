# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 23:16:54 2020

@author: Logan Rowe

methods:
    hash
    insert
    find
    remove
"""

INITIAL_CAPACITY=50

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class HashTable:
    def __init__(self):
        self.capacity=INITIAL_CAPACITY
        self.size=0
        self.buckets=[None]*self.capacity
        
    def hash(self,key):
        hashsum=0
        for idx,c in enumerate(key):
            hashsum +=(idx+len(key))**ord(c)
            hashsum = hashsum%self.capacity
        return(hashsum)
        
    def insert(self,key,value):
        self.size+=1 #because we added an element
        index=self.hash(key)
        node=self.buckets[index]
        
        if node is None:
            self.buckets[index]=Node(key,value)
            return
        
        prev=node
        while node!=None:
            prev=node
            node=node.next
        
        prev.next=Node(key,value)
        
    def find(self,key):
        index=self.hash(key)
        node=self.buckets[index]
        while node is not None and node.key!=key:
            node=node.next
        
        #key was not found
        if node is None:
            return None
        else:
            return node.value
        
    def remove(self,key):
        index=self.hash(key)
        node=self.buckets[index]
        
        prev=node
        while node and node.key!=key:
            prev=node
            node=node.next
        
        if node is None:
            return None
        else:
            self.size-=1 #update size of table
            result=node.value
            if prev is not None:
                prev.next=prev.next.next
            else:
                node=None
                
        #return the removed node
        return result 
    
    def inspect(self,buckets):
        '''
        Return all elements in a bucket
        '''
        elements={}
        for index in buckets:
            node=self.buckets[index]
            while node is not None:
                elements[node.key]=node.value
                node=node.next
        return elements

if __name__=='__main__':
    hash_table=HashTable()
    hash_table.insert('ada',{'age':87,'profession':'mathematics'})
    print(hash_table.find('ada'))
    print(hash_table.inspect([i for i in range(50)]))