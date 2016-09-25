#Write a program to calculate the credit card balance after one year if a person only pays the minimum 
#monthly payment required by the credit card company each month.
#MIT P.set 2, program a
#Author: Joshua Steier
#9/25/2016, 10:16 am
#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#let's have a variable called month, and totalpay, monthlyinterestrate, annualinterestrate, minpayment, monthlypayment, balance
month= 0
#start month and total pay at 0
#some variables don't need to be defined yet, the MIT checker will generate it's own tests.
totalpay= 0
#arithmetic expression for monthly interest rate
monthlyinterestrate = annualinterestrate / 12.0
#month cannot be greater than 12
while month < 12:
    minpayment = monthlypaymentrate * balance
    unpaybalance= balance - minpay
    totalpay = totalpay + minpay
    balance = unpaybalance + (monthlyinterestrate * unpaybalance)
    month = month + 1
    print("Month: " + str(month))
    #in the problem set, it stated to round to two decimal places
    print("Min monthly pay:  " + str(round(minpayment, 2)))
    print("Remaining balance: " + str(round(balance, 2)))
print("Total paid: " + str(round(totalpay, 2)))
print("Remaining balance: " + str(round(balance,2)))