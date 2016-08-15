#This program will compute the factorial of a number
#for ex: 4! is 4 * 3 * 2 * 1
# 0!= 1
#Author: Joshua Steier
#Time: 
num = int(raw_input("Enter in a number: \n "))
factorial= 1
if num < 0:
    print "Cannot do factorial for negative numbers\n"
elif num == 0:
    print "zero factorial is 1\n"
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print "The factorial of\n " + str(num) + "   is  " + str(factorial)