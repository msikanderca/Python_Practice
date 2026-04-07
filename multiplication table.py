
# code to display a multiplication table using for loop

tab_number = int(input ("Enter the number of your choice to print the multiplication table: "))

#For loop to iterate the multiplication 10 times and print the table
print ("The Multiplication Table of: ", tab_number)
for count in range(1, 11):
   print (tab_number, 'x', count, '=', tab_number * count)