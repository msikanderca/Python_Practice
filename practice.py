num = int (input("Enter number : ") )

rev = 0
while (num != 0):
    d = num %10
    rev =rev + d
    num = num //10
print (f'total number is {rev}')



