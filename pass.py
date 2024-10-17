'''
File: pass.py
Author: Marco Lopez
Description: Program that calculates a passing grade.
'''

total_points = float(input("How many total points were possible?:"))
points_earned = float(input("How many points did you earn?:"))

grade = (points_earned/total_points)*100

if grade >= 72:
    print(f"That is {grade:.2f}%.\nYou can enroll in data structures.")

elif grade < 72:
    print(f"That is {grade:.2f}%.\nYou should retake CS1.")
