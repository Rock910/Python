#stack implementation in python
#A stack is an abstract data type that uses primarily pop and push with a list of elements
#A stack is a last in first out
#Author: Joshua Steier
#I'll start by creating stack class: I need to check if it's empty or not
#Then ill peek, and I can pop and push elements in the stack
class Stack:
    def __init__(self):
        self.__elements= []
    def isEmpty(self):
        return len(self.__elements) == 0
    #return the top of the stack without removal
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.elements) -1]
    def push(self, value):
         self.__elements.append(value)   
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()
    def getSize(self):
        return len(self.__elements)