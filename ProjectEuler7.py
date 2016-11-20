#project Euler problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#Author: Joshua Steier
#a prime is a number that is greater than 1 and divisible by itself and 1
#What is the 10 001st prime number?
#let's try to list out primes first six and expand to get 10001
def primes(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]
