a=[]
n =int(input('Enter number of elements in the list: '))
for x in range (0,n) :
    value = int (input('Enter element ' +str(x+1) + ":") )
    a.append(value)
#swap first and last elements of the list
a[0],a[len(a)-1]=a[len(a)-1],a[0]
print("New list is ", a)



a1=[]
n1 =int(input('Enter number of elements in the list: '))
for x in range (0,n1) :
    value = int (input('Enter elements' +str(x+1) + ":") )
    a1.append(value)
# using temp variable
temp =a1[0]
a1[0] = a1[n1-1]
a1[n1-1] = temp
print("New list is ", a1)