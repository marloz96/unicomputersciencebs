'''
File: distance.py
Author: Marco Lopez
Description: Program that calculates how long it will take to reach a certain distance.
'''

current_speed = int(input("What is your current speed in MPH?:"))
distance_remaining = int(input("How far do you have left to travel?:"))

minutes_to_destination = ((60*distance_remaining)/current_speed)

print(f"It will take {minutes_to_destination:.1f} minutes to arrive to your destination.")
