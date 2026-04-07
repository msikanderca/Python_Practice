# Python program to separate characters in a given string.
# Program 1: Using a For Loop
str = "Hello Python"
for char in str:
    print(char)
    print("\n")
# Program 2: Using the Join() Method
str1 = "Hello Python"
new_str = "\n".join(list(str1))
print(new_str)

# Program 3: Using a Lambda Function
str2 = "Hello Python"
list(map(lambda x: print(x, "\n"), str2))