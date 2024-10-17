'''
File: countVowels.py
Author: Marco Lopez
Description: Program that counts vowels using string slicing
'''

text = input("Enter the text you want to analyze: ")
length = len(text)

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0


for character in text:
    if character == "a" or character == "A":
        count_a += 1
    elif character == "e" or character == "E":
        count_e += 1
    elif character == "i" or character == "I":
        count_i += 1
    elif character == "o" or character == "O":
        count_o += 1
    elif character == "u" or character == "U":
        count_u += 1

print("There were",count_a,"a's")
print("There were",count_e,"e's")
print("There were",count_i,"i's")
print("There were",count_o,"o's")
print("There were",count_u,"u's")


    
