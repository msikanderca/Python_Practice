#Python program to copy one string to another string.
#Program 1: Copy String using For Loop
string = input("Please Enter a string: ")
new_string = ""
for char in string:
    new_string += char
print("New String:", new_string)

#Program 2: Copy String using Slice Operator
string1 = input("Please Enter a string: ")
new_string1 = string1[:]
print("New String After Copy:", new_string1)

#Program 3: Copy String using Slice Operator
string2 = input("Please Enter a string: ")
new_string2 = str(string2)
print("New String After Copy:", new_string2)