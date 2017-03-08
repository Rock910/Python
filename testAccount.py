# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:24:32 2017

@author: steierjo
"""

#test program for account, id 1122, balabce of 20000, ir of 4.5%, withdraw 2,500, deposit 3,000 print all
from Accountclass import Account
def main():
    annualInterestRate= 4.5
    id = 1122
    balance= 20000
    account = Account(id, balance, annualInterestRate)
    print("The id number is: " , account.getID())
    print("The balance is : " , account.getinitialBalance())
    print("The interest rate is: ", account.getannualIR())
    print("Let's withdraw 2,500: ", account.withdraw(2500))
    print("Let's deposit 3,000: ", account.deposit(3000))
main()