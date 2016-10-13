#Purpose: a helper function for a hangman game, this checks wether or not the word to be found and letters guessed are the same
#Author: Joshua Steier, 10/10/2016, part of MIT problem set
#define isWordGuessed, takes in a secret word and letters guessed
def isWordGuessed(secretWord, lettersGuessed):
    #zeroth index of a string indicates first character
    letters=[secretWord[0]]
    for i in range(0,len(secretWord)):
        if secretWord[i] not in letters:
                letters+=secretWord[i]
    for i in range(0,len(letters)):
        if letters[i] not in lettersGuessed:
            return False
   
    return True
