'''
File: parkingGarage.py
Author: Marco Lopez
Description: Program that calculates change due to person paying for parking
'''

charge_for_parking = float(input("How much to park?:"))
paid_by_customer = float(input("Amount paying:"))

change_due = (paid_by_customer-charge_for_parking)
dollars = (change_due//1)
cents = ((change_due%1)/.25)

print(f"Change is",dollars,"dollars and", cents,"quarters.")

