'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

#Solved by Shashwat Raj

u=2000
v=3200
for i in range(u,v):
    if i%7==0 and i%5!=0:
        print(i, end=',')
