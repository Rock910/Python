# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:12:23 2017

@author: steierjo
"""

#linkedpriorityqueue
from node import Node
from linkedqueue import LinkedQueue
class LinkedPriorityQueue(LinkedQueue):
    def __init__(self, sourceCollection= None):
        LinkedQueue.__init__(self, sourceCollection)
        
    def add(self, newItem):
        if self.isEmpty() or newItem >= self._rear.data:
         LinkedQueue.add(self, newItem)
        else:
            probe= self._front
            while newItem >= probe.data:
                trailer= probe
                probe= probe.next
            newNode= Node(newItem, probe)
            if probe==self._front:
                self._front = newNode
            else:
                trailer.next= newNode
            self._size +=1
            