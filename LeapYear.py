# Python Program to check the given year is a leap year or not.
# Method 1: Check Leap Year Using if else in Python

year = int(input("Please Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Method 2: Check Leap Year Using ternary operator Python
year1 = int(input("Please Enter a year: "))
leap_year1 = "Leap year" \
    if ((year1 % 4 == 0 and year1 % 100 != 0)
        or year1 % 400 == 0) else "Not a leap year"
print(leap_year1)

# Method 3: Using Calendar module of Python
import calendar
year2 = int(input("Please Enter a year: "))
leap_year2 = "Leap year" if calendar.isleap(year2) else "Not a leap year"
print(leap_year2)