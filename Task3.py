"""
Есть список numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
Вывести все нечетные числа больше 50, используя функцию filter().
"""


def my_func(num):
    return num > 50 and num % 2 == 1


numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
new_numbers = list(filter(my_func, numbers))
print(new_numbers)
