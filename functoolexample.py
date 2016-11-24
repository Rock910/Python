#example of using partial from the functools package, very useful in functional programming with python
#Author: Joshua Steier
from functools import *
def functionguy(a, b, c):
    return a,b,c
p_function= partial(functionguy, 10)
p_function(3,4)
#expected output is 10, 3, 4
p_function = partial(functionguy, 10, 12)
p_function(3)