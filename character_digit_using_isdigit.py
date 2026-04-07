# Python program to check given
# character is digit or not using isdigit() method.

# taking input from user
ch = input("Enter a character : ")
# checks if character ‘ch’ is digit or not
if(ch.isdigit()):
     #if ‘ch.digit()’ returns “True”
    print("The Given Character ", ch, "is a Digit")
else:
      #if ‘ch.digit()’ returns “False”
    print("The Given Character ", ch, "is not a Digit")
