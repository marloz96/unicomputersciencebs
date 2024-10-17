'''
File: fuelSavings.py
Author: Marco Lopez
Description: Program that calculates the amount of money saved by buying
a new car!
'''

miles_per_year = int(input("Please enter the miles you drive per year:"))
mpg_current_car = float(input("Please enter the MPG in your current car:"))
mpg_new_car = float(input("Please enter the MPG in the new car:"))
cost_of_gas = float(input("Please enter the current price of gas:"))

fuel_cost_current = ((miles_per_year*cost_of_gas)/mpg_current_car)
fuel_cost_new = ((miles_per_year*cost_of_gas)/mpg_new_car)
savings = (fuel_cost_current-fuel_cost_new)

print(f"The fuel cost for your current car:${fuel_cost_current:.2f}")
print(f"The fuel cost for the new car:${fuel_cost_new:.2f}")
print(f"The savings (or loss) you would recieve by buying the new car:${savings:.2f}")
