# Python program to calculate sum of integers in string.
str1 = input("Enter a string: ")
digit_sum = 0

for i in str1:
    if i.isdigit():
        # Adding the digit to the total sum
        digit_sum += int(i)

print("Sum =", digit_sum)