# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код


# def drawing_triangle(start_point_x, start_point_y, start_angle, start_length):
#     zero_point = sd.get_point(start_point_x, start_point_y)
#     draw_line_a = sd.get_vector(zero_point, start_angle, start_length, 3)
#     draw_line_a.draw()
#     draw_line_b = sd.get_vector(draw_line_a.end_point, start_angle + 120, start_length, 3)
#     draw_line_b.draw()
#     draw_line_c = sd.get_vector(draw_line_b.end_point, start_angle + 240, start_length, 3)
#     draw_line_c.draw()
#
#
# drawing_triangle(150, 150, 10, 75)
#
#
# def drawing_square(start_point_x, start_point_y, start_angle, start_length):
#     zero_point = sd.get_point(start_point_x, start_point_y)
#     draw_line_a = sd.get_vector(zero_point, start_angle, start_length, 3)
#     draw_line_a.draw()
#     draw_line_b = sd.get_vector(draw_line_a.end_point, start_angle + 90, start_length, 3)
#     draw_line_b.draw()
#     draw_line_c = sd.get_vector(draw_line_b.end_point, start_angle + 180, start_length, 3)
#     draw_line_c.draw()
#     draw_line_d = sd.get_vector(draw_line_c.end_point, start_angle + 270, start_length, 3)
#     draw_line_d.draw()
#
#
# drawing_square(400, 150, 20, 75)
#
#
# def drawing_pentagon(start_point_x, start_point_y, start_angle, start_length):
#     zero_point = sd.get_point(start_point_x, start_point_y)
#     draw_line_a = sd.get_vector(zero_point, start_angle, start_length, 3)
#     draw_line_a.draw()
#     draw_line_b = sd.get_vector(draw_line_a.end_point, start_angle + 72, start_length, 3)
#     draw_line_b.draw()
#     draw_line_c = sd.get_vector(draw_line_b.end_point, start_angle + 144, start_length, 3)
#     draw_line_c.draw()
#     draw_line_d = sd.get_vector(draw_line_c.end_point, start_angle + 216, start_length, 3)
#     draw_line_d.draw()
#     draw_line_e = sd.get_vector(draw_line_d.end_point, start_angle + 288, start_length, 3)
#     draw_line_e.draw()
#
#
# drawing_pentagon(400, 400, 30, 75)
#
#
# def drawing_hexagon(start_point_x, start_point_y, start_angle, start_length):
#     zero_point = sd.get_point(start_point_x, start_point_y)
#     draw_line_a = sd.get_vector(zero_point, start_angle, start_length, 3)
#     draw_line_a.draw()
#     draw_line_b = sd.get_vector(draw_line_a.end_point, start_angle + 60, start_length, 3)
#     draw_line_b.draw()
#     draw_line_c = sd.get_vector(draw_line_b.end_point, start_angle + 120, start_length, 3)
#     draw_line_c.draw()
#     draw_line_d = sd.get_vector(draw_line_c.end_point, start_angle + 180, start_length, 3)
#     draw_line_d.draw()
#     draw_line_e = sd.get_vector(draw_line_d.end_point, start_angle + 240, start_length, 3)
#     draw_line_e.draw()
#     draw_line_f = sd.get_vector(draw_line_e.end_point, start_angle + 300, start_length, 3)
#     draw_line_f.draw()
#
#
# drawing_hexagon(150, 400, 40, 75)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)


def draw_line(sides, start, stop, angle, length, width):

    zero_point = sd.get_point(start, stop)

    amount_sides_angle = int(360 / sides)

    for i in range(0, 360, amount_sides_angle):
        draw_lines = sd.get_vector(zero_point, angle, length, width)
        draw_lines.draw()
        zero_point = sd.get_point(draw_lines.end_point.x, draw_lines.end_point.y)
        angle += amount_sides_angle


def drawing_figure(start_point_x, start_point_y, start_angle, start_length):

    draw_sides = int(input('How many sides the figure should have? (more than two)\n', ))

    draw_width = int(input('How width of sides the figure should have?\n', ))

    draw_line(draw_sides, start_point_x, start_point_y, start_angle, start_length, draw_width)


drawing_figure(150, 150, 10, 50)

# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)
#   Look here:
#https://ru.stackoverflow.com/questions/1161766/%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D0%BF%D0%BE%D1%8F%D0%B2%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F-%D1%80%D0%B0%D0%B7%D1%80%D1%8B%D0%B2-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9-%D0%B8-%D0%BA%D0%BE%D0%BD%D0%B5%D1%87%D0%BD%D0%BE%D0%B9-%D1%82%D0%BE%D1%87%D0%BA%D0%BE%D0%B9-%D0%BA%D1%80%D1%83%D0%B3%D0%B0

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
