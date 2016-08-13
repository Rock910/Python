#Problem Set 1: Problem 1, First try, note output doesn't work correctly, as per edX course, part of my semi- mit challenge
#Author: Joshua Steier
#Collaborators: None
#Time: 0:40
#The program will prompt user for a string, the string will count and print out the number of vowels
s= raw_input("Enter in a string: \n")
count = 0
for letter in s:
  if letter in "aeiou":
    count+=1
print "Number of vowels:" + str(count)
