# Python program to remove given character from String.
str = input("please enter a string : ")
ch = input("please enter a character : ")
print(str.replace(ch," "))

# Using replace() method
def remove_char(s1,s2):
    print(s1.replace(s2, ''))
s1 = input("please give a String : ")
s2 = input("please give a Character to remove : ")
remove_char(s1,s2)

#Using translate() method
def remove_char1(s11,s21):
    dict = {ord(s21) : None}
    print(s11.translate(dict))
s11 = input("please give a String : ")
s21 = input("please give a Character to remove : ")
remove_char1(s11,s21)