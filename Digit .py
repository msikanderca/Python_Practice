# converting numbers to digits

phone = input ("Enter phone: ")
digit_mapping= {
    "1" : "One" ,
    "2" : "Two" ,
    "3" : "Three",
    "4" : "Four",
}
# if 5 to 9 given print !
output  = ""
for each_char in phone:
    output = output + digit_mapping. get(each_char, " ! ") + " "
print (output)
