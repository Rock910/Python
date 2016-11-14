#second example of functional programming but using filter
#Author: Joshua Steier
#filter essentially "filters out" guys that do or do not belong in a list
#for example, in a list of [3, 2, 1], if I define big to be where guys in the list are > 2, then only 3, would print out
def big(x):
    if x > 2:
        print x
filter(big, [3, 2, 1])
#I can define a small too if I wanted
def small(x):
    if x < 2: 
        print x
filter(small, [3, 2, 1])
#This illustrates usage of filter