#purpose: to play a game of hangman
#author: Joshua Steier 10/10/2016, part of MIT problem set
# this game uses the functions isWordGuessed, getGuessedWord, and getAvaliableLetters, which are all previously defined
#and can be found elsewhere on my github page so that you can impliment them in this code, to play. 

#define hangman, takes as input secretWord
def hangman(secretWord):

#welcome the user in traditional manner
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +" letters long")
    print("-----------")
    lettersGuessed = []
    guesses = 8
    # while all the letters of secretWord are not yet in lettersGuessed and guesses left is more than 0
    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        # print first line
        print("You have " + str(guesses) +" guesses left")
        # print second line
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        # print third line
        # if user input a letter that has already been entered, reprompt for letter
        while True:
            guessLetter = raw_input("Please guess a letter: ").lower()
            if guessLetter in lettersGuessed:
                print(" You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
                print("    You have " + str(guesses) +" guesses left")
                print("Available Letters: " + getAvailableLetters(lettersGuessed))
            else:
                break
        lettersGuessed += guessLetter
        # print last line
        # if correctly guessed secret word
        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            print("Congratulations, you won!")
            break
        # else if the guess letter is in secret word
        elif guessLetter in secretWord:
             print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
             print("-----------")
        # else the guess letter is not in secret word
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            guesses -= 1
        # if ran out of guesses
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
