#Eg for inheritance

class Mammal:
    def  walk(self):
        print("Walk")
class Dog(Mammal):
    pass
class Cat(Mammal):
    def cute(self):
        print ("Cutie")
cat1 = Cat()
cat1.cute()
cat1.walk()



