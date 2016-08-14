#Program will print out if a number is even or odd
#Author: Joshua Steier
#Time: 0:30 Seconds
x= int(raw_input("Enter in an integer: \n"))
if x % 2 == 0 and x > 0:
    print "Even\n"
elif x == 0:
    print "Zero\n"
else:
    print "Odd\n"
