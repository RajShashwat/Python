#Solved by Shashwat Raj
N = int(input())
if N>0 and N<=100:
    if N%2 ==1:
        print("Weird")
    elif N%2 == 0 and N <5 and N>2:
        print("Not Weird")
    elif N%2 == 0 and N <=20 and N>6:
        print("Weird")
    elif N%2==0 and N>20:
        print("Not Weird")
