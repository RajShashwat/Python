#Created by Shashwat Raj
#Program to print highest no of 3 given nos
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if num1>=num2 and num1>=num3:
    print("Gretest number: ",num1)
if num2>=num1 and num2>=num3:
    print("Gretest number: ",num2)
if num3>=num2 and num3>=num1:
    print("Gretest number: ",num3)