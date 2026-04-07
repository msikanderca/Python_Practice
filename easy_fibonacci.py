#fibonacci

n = int (input("enter number :"))
a=0
b=1
for i in range (2, (n-1)):
    c= a +b
    print (c)
    a=b
    b=c
