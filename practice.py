'''
File: avVowels.py
Author: Marco Lopez
Description: average vowels in a word
'''

#ask for input from user

word = input("Enter a word: ")

#keep count of vowels and amount of words being entered

vowel_count = 0
word_count = 0

while word.lower() != "quit":
    for vowel in word.lower():
        if vowel in "aeiou":
            vowel_count += 1
        elif word.lower() == "quit":
            break
    word = input("Enter a word: ")
    word_count += 1

average = vowel_count/word_count
print("The average count of vowels per word is", average)
print("Total amount of vowels is", vowel_count)
