# initializing string
test_string = "1w3e4r5t6y7u7i8i"

# printing original strings
print("The original string : " + test_string)

# using join() + isdigit() + filter()
# Extract digit string
res = ''.join(filter(lambda i: i.isdigit(), test_string))

# print result
print("The digits string is : " + str(res))