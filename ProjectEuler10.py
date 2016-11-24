#Project Eueler problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
#Step1: Generate primes
#I'm gonna try this using a list comprehension
noprimes= [j for i in range(2,8) for j in range(i * 2, 50, i)]
primes= [x for x in range(2, 10) if x not in noprimes]
      
#step 2 sum the primes:
#i'll just try to sum the first 4 primes, which is expected as 17
sum(primes)
#step3: extend the idea for million primes
#Would do but computer would crash.

