'''
File: squares.py
Author: Marco Lopez
Description: Program that uses nested loops to  create a Latin Square
'''

#Step 1 - Ask for two inputs

square_order = int(input("Please enter the order of square: "))
top_left_num = int(input("Please enter the top left number: "))

#Step 2 - Make sure inputs look for garbage inputs

while top_left_num < 1 or top_left_num > square_order:
    print("Invalid top left number.\n")
    top_left_num = int(input("Please enter the top left number: "))

print("The Latin Square is:")

#Step 3 - Use inputs from user to create a Latin Square that still
#works when top_left_num is any number less than square_order

for i in range(top_left_num, square_order+1):
    for j in range(square_order):
        print(i,end=" ")
        i = (i%square_order)+1
    print() 
    


