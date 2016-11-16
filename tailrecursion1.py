#This program uses functional programming(tail recursion) to convert everything in a list to lowercase
#Author: Joshua Steier, 11/15/2016
# if length of the list is zero return zero
def lowerlist(L):
    if len(L) == 0:
        return None
    else:
        print L[0].lower
        return lowerlist(L[1:])