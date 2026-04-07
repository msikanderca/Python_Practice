# code to check factorial
def fact(n):
    res =1
    for i in range (1, n+1):
        res = res * i
    return res


num = int(input("Enter a number: "))
print (f"Factorial of {num} is ", fact(num))

