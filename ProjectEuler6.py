#project Euler question 6


#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#let me print out a range of the natural numbers from 0 to 10 and then impliment a squar eon them with map, and then sum that list
natnums= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squareguys= lambda x: x ** 2
firstguys = (sum(map(squareguys, natnums)))
print(firstguys)
#square the sum of natural guys 
sum(natnums)
secondguy = (sum(natnums ) ** 2)
#subtract the guys 
answer= secondguy - firstguys
print(answer)

#need to extend for the first 100 natrual numbers
#how can i generate a list of 100 natural numbers?
list1= range(1,101)
firstdudes= (sum(map(squareguys, list1)))
print(firstdudes)
secondudes= (sum(list1) ** 2)
answers= secondudes -firstdudes
print(answers)