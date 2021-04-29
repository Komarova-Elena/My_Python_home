"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class NonNumberListValueException(Exception):
    pass


def append_number(number_list: list):
    value = input("Введите число >>> ")

    try:
        number_list.append(float(value))
    except ValueError:
        raise NonNumberListValueException(f"Вы ввели '{value}' вместо числа")


numbers = []

while True:
    try:
        append_number(numbers)
    except NonNumberListValueException as exception:
        print(exception)
    except KeyboardInterrupt:
        print(f"\nСписок чисел = {numbers}")
        break