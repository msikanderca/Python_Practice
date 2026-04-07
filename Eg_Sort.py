my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort()
print(my_list)


# without using sort function
list1 = [6,8,4,2,1,9,5]
nlist1 =[]
while list1:
    min =list1[0]
    for x in list1:
        if x > min:
            min  = x
    nlist1.append(min)
    list1.remove(min)
print(nlist1)
