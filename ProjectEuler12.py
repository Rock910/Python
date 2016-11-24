#Project Euler question number 12: finding the value of the first triangle number that has over 500 divisors, so I'm creating a template.
#Author: Joshua Steier
#Purpose: this function will return the factors of a given number
#I can create factors of numbers, this will be my first step in solving this problem
def printfactors(number):
   #the function printfactors will print out the factors of a given number
   #Args:
   #the input number is going to be a natural number 
   #Returns:
   #a list of numbers that are factors of the given input
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
    #expected output of printfactors(3): 1,3
#Now I need to compute triangle numbers:
#A triangle number is defined as addition of the natural numbers
#I need to sum from 0 to the next number , num is prvoided by the programmer but can be asked for in input
num = 100
#num here represents the ith triangle number, where i = 1, 2, 3,....n
#for example: the 3rd triangle number is 6, if I make n 3
if num <0 :
    print("Enter in a positive number: ")
else:
        sum = 0
        while(num > 0):
            sum += num
            num -= 1
print("The sum is", sum)


    