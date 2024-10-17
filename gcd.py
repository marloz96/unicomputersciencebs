'''
File: gcd.py
Author: Marco Lopez
Description: Program that calculates the Greatest Common Denominator between
2 integers
'''

first_integer = int(input("Enter the first integer:"))
second_integer = int(input("Enter the second integer:"))

if first_integer < second_integer:
    smaller = first_integer
    bigger = second_integer
else:
    smaller = second_integer
    bigger = first_integer

while bigger % smaller != 0:
    remainder = bigger%smaller
    bigger = smaller
    smaller = remainder

print("Greatest common denominator is",smaller)
    
    
