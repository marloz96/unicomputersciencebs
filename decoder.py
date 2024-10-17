'''
File: decoder.py
Author: Marco Lopez
Description: Program that decodes a Caesar Cipher
'''

text = input("Enter a string to decode: ")
rotation_value = int(input("Enter rotation integer between 1-25: "))

alphabet = "abcdefghijklmnopqrstuvwxyz"
word = 0
 

for letter in text:
    if letter in alphabet:
        character = (alphabet.find(str(letter)))-rotation_value
        message = alphabet[character]
        print(message,end="")

    else:
        print(letter,end="")
