'''
File: tip.py
Author: Marco Lopez
Description: Program that calculates a tip
'''

cost_of_meal = float(input("Enter cost of meal:"))

tip = (cost_of_meal*.2)

if tip < 2.50 and tip > 0:
    print("Your tip is: $2.50")

else:
    print(f"Your tip is:{tip:.2f}")
