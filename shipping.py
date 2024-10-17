'''
File: shipping.py
Author: Marco Lopez
Description: Program that calculates shipping cost based on weight of package
and shipping method
'''

shipping_method = input("Enter shipping method:")

while (shipping_method != "s") and (shipping_method != "e") and (shipping_method != "o"):
    print("That choice was not valid. \nPlease try again")
    shipping_method = input("Enter shipping method:")

weight = float(input("Enter shipping weight (kg):"))

standard = (shipping_method == "s")
express = (shipping_method == "e")
overnight =(shipping_method == "o")

small = (weight <= 1)
medium = (weight > 1 and weight <= 5)

if standard:
    if small:
        print("The cost is $5")
    elif medium:
        print("The cost is $10")
    else:
        print("The cost is $20")

elif express:
    if small:
        print("The cost is $10")
    elif medium:
        print("The cost is $20")
    else:
        print("The cost is $40")

elif overnight:
    if small:
        print("The cost is $25")
    elif medium:
        print("The cost is $35")
    else:
        print("The cost is $60")


    
