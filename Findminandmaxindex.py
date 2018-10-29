

#minimum of index
def indexOfMin(lyst):
    #input: list, output int 
    #returns the minimum of the list
    minIndex= 0
    currentIndex= 1
    while currentIndex<len(lyst):
        if lyst[currentIndex]< lyst[minIndex]:
            minIndex= currentIndex
        currentIndex = currentIndex + 1
    return minIndex
#let's make a function for the index max
def indexofMax(lyst):
    #takes in a list: returns a int
    #purpose: to find the index of the maximum element in a list
    
    maxIndex= 0
    currentIndex= 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] > lyst[maxIndex]:
            maxIndex= currentIndex
        currentIndex= currentIndex +1
    return maxIndex
#input: list, output ints            
