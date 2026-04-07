# Write a program in Python to print the
# Fibonacci series using recursive method.
n = int(input("please give a number for fibonacci series : "))
first,second=0,1
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print("fibonacci series are : ")
for i in range(0,n):
    print(fibonacci(i))