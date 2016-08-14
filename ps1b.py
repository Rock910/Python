#Problem Set 1: part b, counting bobs, as per edx course
#Author: Joshua Steier
#Collaborators: None
#Time: 2:00 minutes
#Program will count number of bobs given a string
num = 0
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        num += 1
print 'Number of times bob occurs is:', num