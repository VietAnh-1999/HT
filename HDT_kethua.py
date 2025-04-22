# Khai bo lop cha
class Animal:
    def __init__(self,Type,name):
        self.Type = Type
        self.name = name
    def printMe(self):
        print("TYPE: {}".format(self.Type))
        print("NAME: {}".format(self.name))
    def eat(self):
        print("an")
    
    def makeSound(self):
        print("nhac len")

    def sleep(self):
        print("ngu")

# Clas con
class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,"Dog",name)
        
dog1 = Dog("Muc")
dog1.eat()
dog1.printMe()