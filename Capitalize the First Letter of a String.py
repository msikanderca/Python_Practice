#Python Program to Capialize the First Letter of a String
#defining a capitalize function

def capitalize(String):
    return String.title()

get_capital1 = "hello" # [Hello]
get_capital2 = "python programming" # [Python Programming]
get_capital3 = "python is easy to learn" # [Python Is Easy To Learn]


#Let's print capitalized string from the given strigns
#Capitalized string from first string
print("The Capitalized String Is:  ",capitalize(get_capital1))

#Capitalized string from second string
print("The Capitalized String Is:  ",capitalize(get_capital2))

#Capitalized string from third string
print("The Capitalized String Is:  ",capitalize(get_capital3))
