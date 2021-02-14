# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей   ,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код


# def draw_branches(x, y, angle, length):
#     start_point = sd.get_point(x, y)
#     sd.vector(start_point, angle + 30, length, width=2)
#     sd.vector(start_point, angle - 30, length, width=2)
#
#
# draw_branches(300, 0, 90, 50)

# def draw_branches(x, y, angle, length):
#
#     if length < 10:
#         return
#
#     start_point = sd.get_point(x, y)
#
#     plus_point = sd.vector(start_point, angle + 30, length, width=2)
#     minus_point = sd.vector(start_point, angle - 30, length, width=2)
#
#     next_length = length * 0.75
#     next_plus_angle = angle + 30
#     next_minus_angle = angle - 30
#
#     draw_branches(plus_point.x, plus_point.y, next_plus_angle, next_length)
#     draw_branches(minus_point.x, minus_point.y, next_minus_angle, next_length)
#
#
# draw_branches(300, 0, 90, 50)

# def draw_branches(start_point, angle, length):
#
#     if length < 10:
#         return
#
#     plus_point = sd.vector(start_point, angle + 30, length, width=2)
#     minus_point = sd.vector(start_point, angle - 30, length, width=2)
#
#     next_plus_point = sd.get_point(plus_point.x, plus_point.y)
#     next_minus_point = sd.get_point(minus_point.x, minus_point.y)
#     next_length = length * 0.75
#     next_plus_angle = angle + 30
#     next_minus_angle = angle - 30
#
#     draw_branches(next_plus_point, next_plus_angle, next_length)
#     draw_branches(next_minus_point, next_minus_angle, next_length)
#
#
# root_point = sd.get_point(300, 30)
#
# draw_branches(root_point, 90, 100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

def draw_branches(start_point, angle, length):

    if length < 10:
        return

    plus_point = sd.vector(start_point, angle + 30, length, width=2)
    minus_point = sd.vector(start_point, angle - 30, length, width=2)

    next_plus_point = sd.get_point(plus_point.x, plus_point.y)
    next_minus_point = sd.get_point(minus_point.x, minus_point.y)
    next_length = length * (0.75 + (sd.random_number(-15, 15) / 100))
    next_plus_angle = angle + 30 + sd.random_number(-12, 12)
    next_minus_angle = angle - 30 - sd.random_number(-12, 12)

    draw_branches(next_plus_point, next_plus_angle, next_length)
    draw_branches(next_minus_point, next_minus_angle, next_length)


root_point = sd.get_point(300, 30)

draw_branches(root_point, 90, 100)

# Пригодятся функции
# sd.random_number()

sd.pause()


