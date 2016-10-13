#purpose: to determine the frequency of certains words in song lyrics
#Author: Joshua Steier 10/10/2016, 2:55 PM
#User must create a txt file, and specify where exactly the txt file is: i.e. your directory, "C: \Users\steierjo.... is my directory
#To find your directory: you can open up the command prompt and it should say.
#The program will ask for the name of your file, read it in
#using a dictionary in python, will account for strange characters, and will account for uppercase/lowercase
#if the program is buggy or does not work, please contact me.
#define our main function that will read in the file and convert everything to lowercase, and sort each item
def main():
    filename= input("Enter in a filename: ").strip()
    infile= open(filename, "r")
    wordCounts= {}
    for line in infile:
        processLine(line.lower(), wordCounts)
    pairs= list(wordCounts.items())
    items= [[x,y] for (y,x) in pairs]
    items.sort()
    for i in range(len(items) -1, len(items) -11, -1):
        print(items[i][1] + "\t" + str(items[i][0]))
#we define a helper function here: called processLine that is used in the main, we need it to call the split method on line, and increment the wordcount/leave it at 1
def processLine(line, wordCounts):
    line= replacePunctuations(line)
    words= line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
#this is another helper function called replace punctuations, this accounts for weird characters in the txt file and simple replaces them with " " using the replace method
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_+=~<>?/,.;:!{}[]|'\"":
            line= line.replace(ch, " ")
        return line
main()
