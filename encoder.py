'''
File:encoder.py
Author: Marco Lopez
Description: program that implements the Caesar Cipher using
user input to endcode and decode the string
'''

#ask user for inputs and make sure inputs are always lowercase

text = input("String to encode: ")
rotation_value = int(input("Enter the rotation value: "))
encode = text.lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"
word = 0
 

for letter in text:
    if letter in alphabet:
        character = (alphabet.find(str(letter)))+rotation_value
        if character > 25:
            message = alphabet[character%26]
        else:
            message = alphabet[character]
        print(message,end="")

    else:
        print(letter,end="")
        

    





    

