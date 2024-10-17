
import math

number_one = int(input("Enter a number (n):"))

while number_one < 0:
    print("invalid\n")
    number_one = int(input("Enter a number:"))
    
number_two = int(input("Enter another number (k):"))

while number_one and number_two >= 0:
    print(math.factorial(number_one),"is",number_one,"!")
    print(math.factorial(number_two),"is",number_two,"!")
    print("nCk =",math.comb(number_one,number_two))
    print("nPk =",math.perm(number_one,number_two))
    number_one = int(input("Enter a number:"))
    number_two = int(input("Enter another number:"))
    
        


    
