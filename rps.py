'''
File: rps.py
Author: Marco Lopez
Description: A program that plays the user in a game of rock,paper,scissors
'''
#create variables to keep count and to allow computer to select option

import random
user_W = 0
computer_W = 0
tie = 0

#state available options for user and ask for input

print("Each round you must select from one of the following weapons:")
print("Enter r for rock\nEnter p for paper\nEnter s for scissors\nEnter q to quit")

weapon = input("Please enter your weapon of choice: ")
    
#create scenarios for each valid input, counting up total wins,losses, and draws

while weapon.lower() != "q":
    for picked in random.choice(["r","p","s"]):
        if picked == "r" and weapon.lower() == "s":
            print("COMPUTER WINS! Human pick:",weapon.lower(),"Computer pick:",picked)
            computer_W += 1
            weapon = input("Please enter your weapon of choice: ")

        elif picked == "p" and weapon.lower() == "r":
            print("COMPUTER WINS! Human pick:",weapon.lower(),"Computer pick:",picked)
            computer_W += 1
            weapon = input("Please enter your weapon of choice: ")
                
        elif picked == "s" and weapon.lower() == "p":
            print("COMPUTER WINS! Human pick:",weapon.lower(),"Computer pick:",picked)
            computer_W += 1
            weapon = input("Please enter your weapon of choice: ")
                
        elif picked == "r" and weapon.lower() == "p":
            print("HUMAN WINS! Human pick:",weapon.lower(),"Computer pick:",picked)
            user_W += 1
            weapon = input("Please enter your weapon of choice: ")
                
        elif picked == "p" and weapon.lower() == "s":
            print("HUMAN WINS! Human pick:",weapon.lower(),"Computer pick:",picked)
            user_W += 1
            weapon = input("Please enter your weapon of choice: ")

        elif picked == "s" and weapon.lower() == "r":
            print("HUMAN WINS! Human pick:",weapon,"Computer pick:",picked)
            user_W += 1
            weapon = input("Please enter your weapon of choice: ")
                
        elif picked == weapon.lower():
            print("TIE. Both picked",weapon)
            tie += 1
            weapon = input("Please enter your weapon of choice: ")

        elif weapon.lower() != "r" and weapon.lower() != "p" and weapon.lower() != "s":    
            print("ERROR. That's not a valid choice.")
            weapon = input("Please enter your weapon of choice: ")

#print quit scenario outputting stats of the game

print("Thanks for playing.\nWe played a total of",(user_W+computer_W+tie),"rounds.")
print("Total ties = ",tie)
print("Total wins for human = ",user_W)
print("Total wins for computer = ",computer_W)

