#Solved by Shashwat Raj
def is_leap(year):
    leap = False
    if year >=1900 and year <=100000:
        if year % 4 == 0:
            leap = True
            if year % 400 != 0 and year % 100 == 0 :
                leap=False
    return leap
year = int(input())
print(is_leap(year))
