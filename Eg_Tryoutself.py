str = 'India'
print(str[-1])
print(str[:-1])
print(str[::-1])
#combine 2 lists to 1 string
list1 = ['my','name']
list2 = ['is', 'john']
list3 = list1 + list2
print(list3)
print(' '.join(list3))

#combine 2 lists to dict
l1 = ['a','b','c']
l2 = [1,2,3]
l3 = dict(zip (l1,l2)) # this will zip with dict
print(dict(l3))
l4 = {l1[i] : l2[i] for i in range (len (l1))}
print(l4)

#count number of times a class is called
class A:
    count =0
    def __init__(self):
        A.count +=1
        print('Class A is called')
a1 = A()
a2 = A()
a3 = A()
print(A.count)

#use global variable to count number of times a class is called
c1=0
class B:
    def __init__(self):
        global c1
        c1 +=1
        print('Class B is called')
b1 = B()
b2 = B()
print(c1)

#duplicate char in string
li = ['India','is','my','country']
str1 = ''.join (li)
print(str1)
dup = []
for char in str1:
    if str1.count(char) >1 and char not in dup:
        dup.append(char)
print(dup)
print(*dup)

#print unique char in str
s = 'test'
unique = []
for char in s:
    if s.count(char) == 1 and char not in unique:
        unique.append(char)
print(unique)

#print output of below program
class w:
    def demo(self):
        print("In Class W")
class x(w):
    def demo(self):
        print("In Class x")
class y(w):
    def demo(self):
        print("In Class y")
class z(x,y):
    pass
test = z()
test.demo()

#one line for loop
al =['india','is','my','country']
bl = [word for word in al if word.startswith ('i')]
print(bl)


