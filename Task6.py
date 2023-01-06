"""
Есть класс Animal c одним методом voice().
class Animal:
def voice(self):
pass
1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().
"""


class Animal:
    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        return 'Мяяяууу'


class Dog(Animal):
    def voice(self):
        return 'Гав-гав'


class Cow(Animal):
    def voice(self):
        return 'Мууу'


my_cat = Cat()
print(f'Кошечка говорит "{my_cat.voice()}"')

my_dog = Dog()
print(f'Собачка говорит "{my_dog.voice()}"')

my_cow = Cow()
print(f'Коровка говорит "{my_cow.voice()}"')
