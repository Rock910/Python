#using the chain in itertools, it attaches one list to another

from itertools import *
for i in chain([1, 2, 3], ["a", "b", "c"]):
    print i
    #expected output is: 1, 2, 3, a, b, c
for i in chain(["johnny appleseeds".split()], [1, 2, 3]):
    print i
for i in izip(["a", "b", "c", "d"], [1,2,3,4]):
    print i
for i in repeat(["over nd over and over"], 5):
    print i
    
    