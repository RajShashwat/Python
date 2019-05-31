'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

#Solved by Shashwat Raj

String=input()
Count={"upper":0,"lower":0}
for i in String:
    if i.isupper():
        Count["upper"]+=1
    elif i.islower():
        Count["lower"]+=1
print("UPPER CASE ",Count["upper"])
print("LOWER CASE ",Count["lower"])
