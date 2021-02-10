# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

from district.central_street.house1.room1 import folks as central_folks_room_1_1
from district.central_street.house1.room2 import folks as central_folks_room_1_2
from district.central_street.house2.room1 import folks as central_folks_room_2_1
from district.central_street.house2.room2 import folks as central_folks_room_2_2

from district.soviet_street.house1.room1 import folks as soviet_folks_room_1_1
from district.soviet_street.house1.room2 import folks as soviet_folks_room_1_2
from district.soviet_street.house2.room1 import folks as soviet_folks_room_2_1
from district.soviet_street.house2.room2 import folks as soviet_folks_room_2_2


central_district_folks = central_folks_room_1_1 +\
                         central_folks_room_1_2 +\
                         central_folks_room_2_1 +\
                         central_folks_room_2_2

soviet_district_folks = soviet_folks_room_1_1 +\
                        soviet_folks_room_1_2 +\
                        soviet_folks_room_2_1 +\
                        soviet_folks_room_2_2

print('На районе живут:', ', '.join(central_district_folks))

print('На районе живут:', ', '.join(soviet_district_folks))


