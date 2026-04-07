#fibonacci
a = 0
n = int(input("Enter the end number to fibonacci series:"))
b = 1
next = b
count = 1
while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print ("")

# using function

def F(num):
    if num == 0: return 0
    elif num == 1: return 1
    else: return F(num-1)+F(num-2)
x = int(input("Enter the end number to fibonacci series:"))
for x in range(0,x):
  print(F(x))