# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 19:55:18 2017

@author: steierjo
"""

#Creation of the ATM Machine, step 1: creation of the account class
#An account class is one of: 
    #a private int data field named id for the account
    # a private float data field named balance for the account
    # a private float data field named annualInterestRate that stores the current IR
    # A constructor that creates an account with specified id(default 0), initial 
    #balance(default 100), and annual interest rate(default 0)
    #the acessor and mutator methods for id balance and interest rate
    # a method named getmonthly interest rate
    # a method named getmonthlyinterest
    # a method named withdraw
    # a method named deposit
#begin with defining the class
class Account:
    def __init__(self, id = 0, balance= 100, annualInterestRate= 0):
        self.__id= id
        self.__initialbalance= balance
        self.__annualInterestRate= annualInterestRate
    def getID(self):
        #getID returns the ID of account
        return self.__id
    def setID(self, id):
        #setID: given an id, sets the current id to be the id inputted
        self.__id= id
    def getinitialBalance(self):
        #returns the initial balance
        return self.__initialbalance
    def setinitialBalance(self, balance):
        self.__initialbalance= balance
    def getannualIR(self):
        return self.__annualInterestRate
    def setannualIR(self, annualInterestRate):
        self.__annualInterestRate= annualInterestRate
    def getMonthlyInterestRate(self):
        dummyvar= self.__annualInterestRate / 100
        return dummyvar / 12
    def getMonthlyInterest(self):
        return self.__initialbalance * self.getMonthlyInterestRate
    def withdraw(self, amount):
        return self.__initialbalance - amount
    def deposit(self, amount):
        return self.__initialbalance + amount
