 '''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе
'''

my_list = [3, 'text', 156, 77.5, None]

for item in my_list:
    print(type(item))