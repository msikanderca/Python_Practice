# Python program to convert lowercase char to uppercase of string.
string = input("Enter a String : ")
result=''
for i in string:  #iterate through each letter/character from the string
        if i.islower():  #if lowercase
            i = i.upper() #converting lowercase into uppercase letter
        result += i #concatenating each character of the string without lowercase letter
print("String after converting lowercase to upper :",result)