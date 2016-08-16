#Program: will take in an n that represents the number of sides a polygon has
#and an s, which represents the length of each side
#the formula for the area of the polygon is assigned to the x
#the perimeter of the polygon is (s * n) squared, and the answer is rounded to 4 decimal places
#Author: Joshua Steier
#Time: 2:00 minutes
#input: float n,  float s -> float
import math
#prompt user for input
n = float(raw_input("Enter in a number for n: \n"))
s = float(raw_input("Enter in a number for s: \n"))
#function definition
def polysum(n, s):
     x= (0.25 * n * (s * s))/(math.tan(math.pi/n)) 
     return round((x + ((s * n)**2)), 4)
      
print polysum(n,s)