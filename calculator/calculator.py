
import os
import re
from dotenv import load_dotenv
load_dotenv()
username = os.getenv('username')
password = os.getenv('password')
print(username)
print(password)
def add(x, y):
    return int(x) + int(y)
def subtract(x, y):
    return int(x) - int(y)
def multiply(x, y):
    return int(x) * int(y)
def divide(x, y):
    return int(x) / int(y)


string=input("enter the string:")    
number=re.findall(r'\d+', string)
print(number)    

print(int(number[0])*int(number[1]))
for i in range(3):
    u = input("enter username:")
    p = input("enter password:")
    if u == username and p==password:
        num1, op, num2 = input("Enter three values: ").split()

        if op == '+':
            print(num1, "+", num2, "=", add(num1, num2))
        elif op == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif op == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif op == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))       
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    