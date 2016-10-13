#purpose: to find the number of trailing zeroes for a number x factorial
#Author: Joshua Steier
#10/9/2016
def zeroes(x):
    five = 0
    for number in range(2, x + 1):
        while number > 0:
            if number % 5 ==0:
                five= five + 1
                number = number / 5
            else:
                break
    return five