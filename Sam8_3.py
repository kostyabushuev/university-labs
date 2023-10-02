class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed
    def run(self):
        print(f'Я бегу со скоростью {self.speed}')

class Cat(Animal):
    def __init__(self, name, weight, speed):
        super().__init__(name, weight, speed)
    def meow(self):
        print('Meeeeeeeeeow')

my_cat = Cat('Koshka', 10, 15)
print(my_cat.name)
print(my_cat.weight)
my_cat.meow()