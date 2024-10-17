'''
File: money.py
Author: Marco Lopez
Description: Program that calculates compounding interest per year depending
on user input
'''

money_invested = float(input("Enter amount of money to deposit:"))
interest_percent = float(input("Enter interest percentage rate:"))
interest_rate = interest_percent/100
num_years = int(input("Enter number of years to compute:"))

for i in range(1,num_years+1):
    balance = (money_invested*((1+interest_rate)**i))
    print(f"The balance is: ${balance:.2f} after year",i)
