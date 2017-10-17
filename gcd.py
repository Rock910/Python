#purpose: to compute the gcd of two numbers
#Author: Joshua Steier
#9/19/2016 @ 2:58 PM
#prompt user for input
n1= eval(raw_input("Enter the first integer: "))
n2= eval(raw_input("Enter the second integer: "))
#allow gcd to start at 1
gcd= 1
k=2
while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd= k
    k= k+1
    #print out the results
print("The greatest common divisor for " + str(n1) + " and " + str(n2) + "  is  " + str(gcd))


#another gcd  but using recursion.
#10/17/2017 @ 2:21 PM
def gcdRecur(a,b):
    #a, b positive ints, and returns a pos int, the gcd
    #let's deal with base case
    if b ==0:
        return a
    else:
        return gcdRecur(b, a%b)
    
