# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:51:02 2017

@author: Joshua Steier, Joshua Talamayan, Davis Cook
"""

#ATM machine directions: use the account class to simulate an atm machine.
#Createten accounts, in a list with ids 0 to 9, and balance of 100
#System prompts user for an id, if incorrect, we ask for a correction, 
#Once accepted the main menu is made, choice 1 is balance
#2 is withdraw
#3 deposit
#4 exit
#let's start by importing the account class
from Accountclass import Account
#we want 10 accounts 
for i in range(10):
    accountlist= []
    accountlist.append(account(id= i))
    #the class atm takes in the class account
class ATM(Account):
    def __init__(self, id):
        super().__init__()
        self.__id= id
        #let's create a main menu
    def mainMenu(self):
        return "Main Menu \n1: Check balance \n2: Withdraw \n3: Deposit \n4: Exit"
def main():
    idInput= eval(input("Enter in your ID: "))
    ATMSim= ATM(idInput)
    print(ATMSim.mainMenu())
    choiceInput = eval(input("Enter a choice please: "))
    if choiceInput == 1:
        print(ATMSim.getinitialBalance())
    elif choiceInput == 2:
        a= eval(input("Enter in an amount to withdraw: "))
        ATM.Sim.withdraw(a)
    else:
        None
 main()       
    
    
        
    
