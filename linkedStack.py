# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:43:02 2017

@author: steierjo
"""

#linkedstack 
from node import Node
from abstrackstack import AbstractStack
class LinkedStack(AbstractStrack):
    
    def __init__(self, sourceCollection= None):
        self._items = None
    AbstractStack.__init__(self, sourceCollection)
    
    def __iter__(self):
        def visitNodes(node):
            if not node is None:
                visitNodes(node.next)
                tempList.append(node.data)
        tempList= list()
        visitNodes(self._items)
        return iter(tempList)
    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is empty! ")
        return self._items.data
        
    def clear(self):
        self._size= 0
        self._items = None
    def push(self, item):
        self._items = Node(item, self._items)
        self._size +=1
    def pop(self):
        if self.isEmpty():
            raise KeyError("The stack is empty!")
        oldItem= self._items.data
        self._items = self._items.next
        self._size -=1
        return oldItem
        
        
        
        
            
        