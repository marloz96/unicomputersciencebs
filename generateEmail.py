'''
File: generateEmail.py
Author: Marco Lopez
Description:
'''

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

email =(last_name[0:5]+first_name[0])
address = "@uni.edu"

print("Your email is",email+address)
