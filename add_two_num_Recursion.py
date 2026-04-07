# Python Program to add two number using recursion.
def add(num1, num2):
    if num2 == 0:
        return num1
    else:
        return add(num1 ^ num2, (num1 & num2) << 1)
num1 = 5
num2 = 7
result = add(num1, num2)
print("The sum of", num1, "and", num2, "is", result)