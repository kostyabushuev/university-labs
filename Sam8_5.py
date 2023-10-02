class Animal:
    def make_noise(self):
        pass

class Cat(Animal):
    def make_noise(self):
        print('Meow... Meow... Meow')

class Dog(Animal):
    def make_noise(self):
        print('Woof... Woof... Woof')

my_cat = Cat()
my_dog = Dog()

my_cat.make_noise()
my_dog.make_noise()