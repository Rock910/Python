## http://inventwithpython.com/hacking (BSD Licensed)
#this program will crack a cesar cipher using brute force
#these comments are entirely my own
#declare a message to be decrypted
message= "GUVF VF ZL FRPERG ZRFFNTR"
#let the letters be those of the english alphapbet, there are 26
LETTERS= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for key in range(len(LETTERS)):
    translated = " "
    for symbol in message:
        if symbol in LETTERS:
            #use the find method to find symbol
            num = LETTERS.find(symbol)
            num = num - key
            #handle the problem of greater than 26 or 0, will wrap around
            if num < 0 :
                num = num + len(LETTERS)
            translated= translated + LETTERS[num]
        else:
           translated= translated + symbol
    print("Key #%s: %s" %(key, translated))
    #display all keys, the one that appears to be english is the answer