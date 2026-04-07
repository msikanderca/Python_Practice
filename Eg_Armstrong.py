#code to check the armstrong number.
num = int(input("Enter the number to check armstrong number: "))
# Assigning the num value to arms
arms = num
# Finding the length of the number
length = len(str(num))
sum1 = 0
# Iterating the values to check armstrong number
while num != 0:
    rem = num % 10
    sum1 = sum1 + (rem ** length)
    num = num // 10
# Printing the result whether the given number is armstrong number or not
if arms == sum1:
    print("The given number", arms, "is armstrong number")
else:
    print("The given number", arms, "is not an armstrong number")





