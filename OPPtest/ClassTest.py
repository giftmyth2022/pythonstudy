class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("My name is %s and %d years old and I an %s" %(self.name,self.age,self.__class__.__name__))

class dog(Animal):
    pass

class cat(Animal):
    def __init__(aaaaa):
        print("I am a cat")

class LittleCat(cat):
    def __init__(self):
        print("I am Just a little cat")
    pass




c = Animal("xiaomiao",20)
c.eat()
d = dog("niuniu",25)
d.eat()