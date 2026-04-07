# Remove duplicate from the list
number = [10,5,7,18,4,20,5,7,4]
final_number =[]
for list in number:
    if list not in final_number:
        final_number.append(list)
print (final_number)

