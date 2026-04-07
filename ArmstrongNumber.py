# Write a program in Python to check whether
# an integer is Armstrong number or not.
# Program 1: Check Armstrong Using a While Loop
num = int(input("Please give a number: "))
sumA = 0
temp = num
# count the number of digits in input
count = len(str(num))
# loop on each digit and calculate the sum
while temp > 0:
    digit = temp % 10
    sumA += digit ** count
    temp //= 10
# check if the number is an Armstrong or not
if num == sumA:
    print("Given ",num, "is an Armstrong number")
else:
    print("Given ",num, "is not an Armstrong number")

# Program 2: Armstrong Using List Comprehension
num1 = int(input("Please Enter a Number: "))
digits1 = [int(digit1) for digit1 in str(num1)]
count = len(digits1)
sumt = sum([digit1 ** count for digit1 in digits1])
if num1 == sumt:
    print("Given ", num1, "is an Armstrong number")
else:
    print("Given ", num1, "is not an Armstrong number")
