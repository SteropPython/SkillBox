# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 1000)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

# point = sd.get_point(500,500)
# rad = 60
# for _ in range(3):
#   sd.circle(point, rad)
#   rad -= 5

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

# def bubble(x,y,step):
#     point = sd.get_point(x,y)
#     rad = 60
#     for _ in range(3):
#         sd.circle(point, rad)
#         rad += step

# bubble(500,500,45)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# rad = 30

# x, y, z = 35, 35, -35

# for i in range(10):
#     z += 2 * x
#     point = sd.get_point(z,y)
#     sd.circle(point, rad)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# rad = 30

# x, y = 35, 35

# for j in range(3):
#     z = -35
#     for i in range(10):
#         z += 2 * x
#         point = sd.get_point(z,y)
#         sd.circle(point, rad)
#     y += rad * 4

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

for _ in range(100):
    radiusCircle = sd.random_number()
    pointCircle = sd.random_point()
    colorCircle = sd.random_color()
    sd.circle(pointCircle, radiusCircle, color=colorCircle)

sd.pause()


