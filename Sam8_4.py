class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed
    def run(self):
        print(f'Я бегу со скоростью {self.speed}')

class Cat(Animal):
    def __init__(self, name, weight, speed, tail_length):
        super().__init__(name, weight, speed)
        self.__tail_length = tail_length
    def meow(self):
        print('Meeeeeeeeeow')
    def wag_tail(self):
        print(f'Хвост размером {self.__tail_length} виляет кошкой')

my_cat = Cat('Koshka', 10, 15, 10)
# print(my_cat.__tail_length) защищённый аттрибут
my_cat.wag_tail()