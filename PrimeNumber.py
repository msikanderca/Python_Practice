# Write a program in Python to check given number is prime or not.

# Method 1: Check Prime Using For Loop
n = int(input("please give a number : "))
i,temp=0,0
for i in range(2,n//2):
    if n%i == 0:
        temp=1
        break
if temp == 1:
    print("given number is not prime")
else:
    print("given number is prime")