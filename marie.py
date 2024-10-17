'''
File: marie.py
Author: Marco Lopez
Description: MARIE assembly language program that calculates sum of positive
and negative numbers, ouputing both sums.
'''

number = int(input("Enter a number: "))
pos_sum = 0
neg_sum = 0

while number != 0:
    if number > 0:
        pos_sum = pos_sum + number
        number = int(input("Enter a number: "))
    elif number < 0:
        neg_sum = neg_sum + number
        number = int(input("Enter a number: "))


print("Your sum for the positive numbers is:", pos_sum)
print("Your sum for the negative numbers is:", neg_sum)
