import converters_inhetitence
from converters_inhetitence import kg_to_lbs


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoyin(self):
        print("annoying")


dog = Dog()
dog.bark()
dog = Cat()
dog.be_annoyin()
dog.walk()
print("============================")
print(kg_to_lbs(100))
print(converters_inhetitence.kg_to_lbs(70))

