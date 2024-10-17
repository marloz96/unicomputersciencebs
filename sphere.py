"""
File: sphere.py
Author: Marco Lopez
Description: A program to calculate the circumfrerence of a
sphere given it's radius.
"""

PI = 3.14159

radiusString = input("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2*PI*radiusInteger
area = PI*(radiusInteger**2)

print("The circumference is:", circumference)
print("The area is:", area)

diameter = (radiusInteger*2)
surfaceArea = (4*PI*(radiusInteger**2))
volume = (((4/3)*PI)*(radiusInteger**3))

print("The diameter is:", diameter)
print("The surface area is:", surfaceArea)
print("The volume is:", volume)

