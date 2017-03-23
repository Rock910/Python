# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:37:52 2017

@author: steierjo
"""

#doubly linked list implementation in python
#what is  a doubly linked list? running time?
class Node(object):
    
    
    
    def__init__(self, data, prev, next):
        self.data= data
        self.prev= prev
        self.next= next
        
        
        
class DoubleList(object):
    head= None
    tail = None
    
    def append(self, data):
        new_node= Node(data, None, None)
        if self.head is None:
            self.head= self.tail = new_node
        else:
            new_node.prev= self.tail
            new+node.next= None
            self.tail.next= new_none
            self.tail= new_node
            
    def remove(self, node_value):
        current_node= self.head
        
        while current_node is not None:
            if current.node.data == node_value:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head= current_node.next
                    current_node.next.prev = None
            current_node= current_node.next
            
    def show(self):
        print" Show list data: "
        current_node= self.head
        while current_node is not None:
            print current_node.prev.data if hasattr(current_node.prev, "data") else None,
            print current_node.data,
            print current_node.next.data if hasattr(current_node.next, "data") else None
            current_node = current_node.next
        print "* " * 50
        
                
        
        