'''
File: maximum.py
Author: Marco Lopez
Description: Program that determines which of the two exams had the higher score
'''

examOne = input("What was your score on the first exam?")
examTwo = input("What was your score on the second exam?")

scoreOne = int(examOne)
scoreTwo = int(examTwo)

if scoreOne>scoreTwo:
    print("Your score of "+examOne+" on the first exam was higher.")

elif scoreTwo>scoreOne:
    print("Your score of "+examTwo+" on the second exam was higher.")

elif scoreOne==scoreTwo:
    print("Your exam scores were exactly the same.")
