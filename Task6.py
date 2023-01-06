"""
Есть класс Animal c одним методом voice().
class Animal:
def voice(self):
pass
1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().

Необходимо дополнить "Практическое задание №6" таким образом,
чтобы в конце программы мы вызвали статический метод родительского класса Animal,
который вывел бы нам количество всех созданных экземпляров.
Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.
"""

class Animal:
    num_of_inst = 0

    def __init__(self):
        Animal.num_of_inst += 1

    def voice(self):
        pass

    def print_num_of_inst():
        print(f'Создано экземпляров класса Animal - {Animal.num_of_inst}')

    print_num_of_inst = staticmethod(print_num_of_inst)


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

Animal.print_num_of_inst()

# Можно вызвать и через инстанс:
my_cow.print_num_of_inst()
