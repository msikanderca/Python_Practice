#functions
def greet_user():
        print("HI")
        print("WELCOME")
print("Start")
greet_user()
print("Stop")
# function with parameter
def hello(name):
        print (f'Hi {name}')
        print ("Welcome")
print ("Call")
hello("Smith")
print ("Drop")
# position argument
def greet_user1(fn, ln):
        print (f'{fn}{ln}')
        print("HI")
        print("WELCOME")
print("Start")
greet_user1("John","smith")
print("Stop")
# Keyword argument
def greet_user2(firstn, lastn):
        print (f'{firstn}{lastn}')
        print("HI")
        print("WELCOME")
print("Start")
greet_user2(lastn="doll",firstn="mary")  #Keyword argument after postional argument
print("Stop")
