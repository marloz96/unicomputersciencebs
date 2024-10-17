'''
File: admit.py
Author: Marco Lopez
Description: Program that calculates ACT and GPA scores to see if you can
be admitted into college.
'''

act_score = float(input("What was your score on the ACT?:"))
hs_gpa = float(input("What was you high school GPA?:"))

if act_score>=23 and hs_gpa>= 1.75:
    print("Congratulations! You can attend Whatsamatta U.")

elif act_score<23 or hs_gpa<1.75:
    print("Sorry. You don't live up to our standards")
