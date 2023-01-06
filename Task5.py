"""
Есть список numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
Используя модуль random, вывести случайный элемент этого списка.
"""

from random import randint

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

rnd_index = randint(0, len(numbers)-1)
print(numbers[rnd_index])
