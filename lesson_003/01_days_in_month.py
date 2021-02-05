# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

# TODO здесь ваш код

if 0 < month < 13:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print('31 day in yours month number')
    elif month in [4, 6, 9, 11]:
        print('30 day in yours month number')
    else:
        print('28 day in yours month number')
else:
    print('Month may be from 1 to 12, jerk')