def getAvailableLetters(lettersGuessed):
   
    notGuessed = []
    # notGuessed = string.ascii_lowercase
    for x in range(26):
        notGuessed += chr(x + ord('a'))

    for y in lettersGuessed:
        notGuessed.remove(y)

    string = ""
    for z in notGuessed:
        string += z
    return string
