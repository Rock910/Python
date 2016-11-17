#task: to cube fibonnaci numbers from 0 to 15 using map
#based off hackerrank problem
#print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
#[4, 3, 3]  
#input: a range that takes the first fibonnaci numbers and cubes them
#Author: Joshua Steier
#need a list of fibonacci numbers :-> cube them
#should create a lambda function to cube the guys first
#ask user for input
n= eval(raw_input("Enter in the number of guys: "))
cubeguys= lambda x: x**3
#let's try it for 5 guys
#let's try to ask for how many number should e printed 0 to 15
fibonaccizerotofif= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 144 + 89, 144 + 89 + 144]
print(list(map(cubeguys, fibonaccizerotofif[0:n])))
#so for example 5 guys prints [0, 1, 1, 8, 27)