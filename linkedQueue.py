# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:09:06 2017

@author: steierjo
"""
#linked Queue, notice same as linked stack but add and pop are updated
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
        self.)items = None
    def push(self, item):
        self._items = Node(item, self._items)
        self._size +=1
    def pop(self):
        oldItem = self._front.data
        self._front= self._front.next
        if self._front is None:
            self._rear = None
        self._size -=1
        return oldItem
        
       
    def add(self, newItem):
        newNode= Node(newItem, None)
        if self.isEmpty():
            self._front= newNode
        else:
            self.rear.next= newNode
        self._rear = newNode
        self._size += 1
        
        