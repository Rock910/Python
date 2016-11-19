#project Euler problem 2: summing even value terms in the fibonacci sequence
#required: a fibonacci sequence, a function to filter out evens, and  sum them 
#let's generate a fibonacci sequence of 15 numbers just for a practice run(ideally this runs for all values less than 4 million but I don't want to crash my computer)
fibonacciguys= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 144 + 89, 144 + 89 + 144]




#filter for even numbers out of a list
def evennumber(x):
    if x % 2 == 0:
        return x
    else:
        return None
evenfib= (filter(evennumber, fibonacciguys))
print(sum(evenfib))
#So if I make a list of [1, 2, 3] I expect [2] to be printed. 
