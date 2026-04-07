#Exceptions

try :
        age = int(input("Enter Age :" ))
        risk = 10000/age
        print(age)
except ValueError:
        print("Invalid data")
except ZeroDivisionError:
        print ("Age can't be zero")