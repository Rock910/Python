#project Euler archived question 1:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#I can make a function for multiples
#One instance of this would be multiples(3, 3) which should print out (0, 3, 6)
def multiples(m, count):
    for i in range(count):
        print(i*m)
print sum(multiples(3, 1000) or (5, 1000))