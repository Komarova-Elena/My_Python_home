a = float(input("Напишите выручку вашей фирмы: "))
b = float(input("Напишите издержки вашей фирмы: "))
c = a - b
d = c / a
if a > b:
    print("Фирма прибыльна")
    print("Прибыль составила:", c)
    print(f"Рентабельость составила: {d :.2f}")
    i = int(input("Напишите количество работников в вашей фирме: "))
    print(f"Прибыль в расчете на 1 сотрудника равна: {(c / i):.2f}")
else:
    print("Фирма убыточна")
    print(a - b)
