#purpose: a helper function for hangman game, if there is a letter from the guessed in the word, it will reveal it but leave others as underscore
#Author: Joshua Steier, 10/10/2016, as part of a MIT problem set
#define the function getGuessedWord, that takes in secretWord string and a list lettersGuessed
def getGuessedWord(secretWord, lettersGuessed):
    a= " "
    #using for loop to iterate over everything starting from index zero to the end of the string
    for i in range(0, len(secretWord)):
        if secretWord[i] in lettersGuessed:
            a= a + secretWord[i]
        else :
            
            a= a + "_"
    return a
