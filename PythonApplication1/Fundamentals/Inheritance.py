class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def meow(self):
        print("meow")

husky = Dog()
husky.bark()
husky.walk()

scottish_fold = Cat()
scottish_fold.meow()
scottish_fold.walk()