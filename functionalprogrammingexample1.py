#Author: Joshua Steier
#program fun using map and reduce
#the program gets the length of each word in the string and makes it into a list(or essentially a map object)
#then reduce sums guys in that object up.
#functional programming example 1
def sumofguys(x,y):
    return x + y
c= map(len, "the overall picture is great".split())
print(c)
print(reduce(sumofguys, c))