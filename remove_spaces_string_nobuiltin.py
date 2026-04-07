# Python program to remove blank space from string.
string = input("Enter a String : ")
result=''
#iterating the string
for i in string:
    #if the character is not a space
    if i!=' ':
        result += i
print("String after removing the spaces :",result)