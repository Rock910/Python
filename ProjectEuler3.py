#project Euler problem 3:
#find the largest prime factor of the number 600851475143
#let's try to make a program that can find prime factors first, and test it on 13195
#n = 13195
#i = 2

#while i * i < n:
   # while n%i == 0:
       # n = n / i
   # i = i + 1

#print (n)
#So this worked as 13195,because it printed out 29 as expected
n= 600851475143
i = 2
while i * i < n:
    while n %i == 0:
        n= n/i
        i = i + 1
print(n)