#Purpose: Create a rectangle class 
#A rectangle is one of:
#width: float
#height: float
#we can find the perimeter, getPerimeter, and area, getArea
#First start with defining the class
class Rectangle(object):
    #now we define our h and w
    def __init__(self, w, h):
        self.w = w
        self.h = h
    #now we can get w and h
    def getWidth(self):
        return self.w
    def getHeight(self):
        return self.h
    #we can compute the perimeter of this rectangle
    def getPerimeter(self):
        return((2 * self.w) + (2 * self.h))
    #we can also compute the area
    def getArea(self):
        return(self.w * self.h)
        
