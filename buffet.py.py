'''
File: buffet.py
Author: Marco Lopez
Description: Program that determines the price of a buffet meal depending on age
'''

customer_age = int(input("Age of customer:"))
cost = 0

while customer_age != -1:
    if customer_age <= 2:
        cost = cost + 0
        customer_age = int(input("Age of customer:"))
    elif customer_age >= 3 and customer_age <=12:
        cost = cost + 4.50
        customer_age = int(input("Age of customer:"))
    elif customer_age >= 65:
        cost = cost + 9.50
        customer_age = int(input("Age of customer:"))
    elif customer_age >= 13 and customer_age <= 64:
        cost = cost + 11
        customer_age = int(input("Age of customer:"))

print(f"Total is: ${cost:.2f}")
    
