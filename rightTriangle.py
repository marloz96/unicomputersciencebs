'''
File: rightTriangle.py
Author: Marco Lopez
Description: Program that uses nest loops to make right triangle
'''

positive_height = int(input("Please input a positive height:"))

while positive_height <= 0:
    positive_height = int(input("Please input a positive height:"))

print("Here is your art.")

for i in range(positive_height):
    for j in range(1,positive_height,1):
        print("*",end=" ")
    print()
