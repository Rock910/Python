#Problem Set 1: MIT Challenge
#Author: Joshua Steier
#:Time: 4: 50 minutes
#This program will print out the 1000th prime 
import math
#make function is_prime to check if it is a prime
def is_prime(a):
    for i in xrange(2, int(math.sqrt(a)+1)):
        if a%i == 0:
            return False
    return True
#while length of primes less than 1000, continue
prime=[]
counts = 2
while len(prime) < 1000:
    if is_prime(counts):
        prime.append(counts)
    counts += 1

print(prime)