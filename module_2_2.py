first = input('Введите число 1: ')
second = input('Введите число 2: ')
third = input('Введите число 3: ')
if first == second == third:
    print(3)
elif first == second:
    print(2)
elif first == third:
    print(2)
elif second == third:
    print(2)
else:
    print('совпадений не найдено')
