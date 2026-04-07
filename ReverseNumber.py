# Write a program to reverse an integer in Python.
# Method 1: Reverse Using While Loop in Python
n = int(input("Please give a number: "))
print("Before reverse your number is : %d" %n)
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10
    n = (n//10)
print("After reverse : %d" %reverse)

# Method 2: Reverse Using String Slicing in Python
num1 = int(input("Please give a number: "))
print("Before reverse your number is : %d" %num1)
rev = int(str(num1)[::-1])
print("After reverse the number:", rev)

# Method 3: Reverse Using Recursion in Python
def reverse1(num2):
    if num2< 10:
        return num2
    else:
        return (num2 % 10) * 10**(len(str(num2))-1) + reverse1(num2 // 10)
num2 = int(input("Please enter a number: "))
print("Before reverse your number is : %d" %num2)
rev1 = reverse1(num2)
print("After reverse the number:", rev1)