'''
File: currencyconverter.py
Author: Marco Lopez
Description: Converts USD to Euros

'''
dollarsString = input("Amount of US Dollars:")
dollarsInteger= int(dollarsString)
Euros = ((dollarsInteger-10)*.781)

print("That amount of US Dollars is equivalent to", Euros,"Euros")

