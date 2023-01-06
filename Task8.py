"""
Необходимо считать любой текстовый файл на вашем ПК (можно создать новый)
и создать на его основе новый файл, где содержимое будет записано в обратном порядке.
В конце программы вывести на экран оба файла - старый в неизменном виде и новый в обратном порядке.
"""

import os


def print_file(file):
    """
    Вывод файла
    :param file: имя файла
    """
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.readlines()
        text = ''.join(data) # создаем из списка строк одну строку
        print(text)
    else:
        print(f'Файл {file} не найден')


def create_reversed_file(file, file_reversed):
    """
    Создание файла со строчками в обратном порядке
    :param file: файл со строчками в прямом порядке
    :param file_reversed: файл со строчкам в обратном порядке
    """

    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.readlines()
        text_reversed = ''.join(data[::-1]) # собираем строки файла в одну строку в обратном порядке
        with open(file_reversed, 'w', encoding='utf-8') as f_rev:
            f_rev.writelines(text_reversed)
    else:
        print(f'Файл {file} не найден')


create_reversed_file('Text.txt', 'Text_reversed.txt')

print('Файл в прямом порядке:\n')
print_file('Text.txt')

print('\nФайл в обратном порядке:\n')
print_file('Text_reversed.txt')