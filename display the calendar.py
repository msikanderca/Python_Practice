# Python program to display calendar

import calendar

# Get the month and year from the users
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Displaying the calendar for the given year and month
print(calendar.month(year, month))
