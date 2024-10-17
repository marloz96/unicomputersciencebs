'''
File: leapyear.py
Author: Marco Lopez
Description: leap year or nah
'''

year = int(input("Enter the year to check if leap year or nah: "))

while year >= 400:
    if (year % 4 == 0):
        if (year%100 != 0) or (year%400 == 0):
            print("Leap year!")
            year = int(input("Enter the year to check if leap year or nah: "))
    else:
        print("Not a leap year!")
        year = int(input("Enter the year to check if leap year or nah: "))
year = int(input("Enter the year to check if leap year or nah: "))
