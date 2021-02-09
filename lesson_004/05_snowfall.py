# -*- coding: utf-8 -*-

import simple_draw as sd

import random

sd.resolution = (1000, 1000)


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 100

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

# points_tuple = []
#
#
# def snowfall_print(point):
#     while point.y > 0:
#         sd.snowflake(point)
#         sd.snowflake(point, color=sd.background_color)
#         point.y -= 5
#
#
# for i in range(N):
#     points_tuple.append(sd.random_point())
#
# for i in range(N):
#     snowfall_print(points_tuple[i])


snowfall_points_tuple = []
snowfall_lengths_tuple = []
snowfall_step_snowfall = 5
snowfall_snowflake_color = []
snowfall_snowflake_angle = []


def snowfall_print(point, lengths, step, color, angle):
    while point.y > 0:
        if sd.user_want_exit():
            break
        sd.snowflake(point, lengths, color, factor_c=angle)
        if point.y < lengths * 0.5:
            break
        sd.snowflake(point, lengths, sd.background_color, factor_c=angle)
        point.y -= step


for i in range(N):
    snowfall_lengths_tuple.append(random.randint(10, 100))

for i in range(N):
    snowfall_snowflake_color.append(sd.random_color())

for i in range(N):
    snowfall_snowflake_angle.append(random.randint(10, 90))

for i in range(N):
    snowfall_points_tuple.append(sd.random_point())

for i in range(N):
    snowfall_print(snowfall_points_tuple[i], snowfall_lengths_tuple[i], snowfall_step_snowfall, snowfall_snowflake_color[i], snowfall_snowflake_angle[i])


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


