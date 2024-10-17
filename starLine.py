'''
File: starLine.py
Author: Marco Lopez
Description: Program that prints out a row of stars using for loops
'''

positive_num = int(input("Please input a positive number:"))

while positive_num <= 0:
    positive_num = int(input("Please input a positive number:"))

print("Here is your art.")

for i in range(0, positive_num):
    print("*", end=' ')

