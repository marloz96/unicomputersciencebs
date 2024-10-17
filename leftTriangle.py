'''
File: leftTriangle.py
Author: Marco Lopez
Description: Program that uses nested loops to print out multiple lines
of stars
'''
positive_height = int(input("Please input a positive height:"))

while positive_height <= 0:
    positive_height = int(input("Please input a positive height:"))

print("Here is your art.")

for i in range(positive_height):
    for j in range(i+1):
        print("*",end=" ")
    print()
