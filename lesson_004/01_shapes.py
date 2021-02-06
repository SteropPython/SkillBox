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


def drawing_triangle(start_point_x, start_point_y, start_angle, start_length):
    zero_point = sd.get_point(start_point_x, start_point_y)
    draw_line_a = sd.get_vector(zero_point, start_angle, start_length, 1)
    draw_line_a.draw()
    draw_line_b = sd.get_vector(draw_line_a.end_point, start_angle + 120, start_length, 1)
    draw_line_b.draw()
    draw_line_c = sd.get_vector(draw_line_b.end_point, start_angle + 240, start_length, 1)
    draw_line_c.draw()


drawing_triangle(150, 150, 10, 75)


def drawing_square(start_point_x, start_point_y, start_angle, start_length):
    zero_point = sd.get_point(start_point_x, start_point_y)
    draw_line_a = sd.get_vector(zero_point, start_angle, start_length, 1)
    draw_line_a.draw()
    draw_line_b = sd.get_vector(draw_line_a.end_point, start_angle + 90, start_length, 1)
    draw_line_b.draw()
    draw_line_c = sd.get_vector(draw_line_b.end_point, start_angle + 180, start_length, 1)
    draw_line_c.draw()
    draw_line_d = sd.get_vector(draw_line_c.end_point, start_angle + 270, start_length, 1)
    draw_line_d.draw()


drawing_square(400, 150, 20, 75)


def drawing_pentagon(start_point_x, start_point_y, start_angle, start_length):
    zero_point = sd.get_point(start_point_x, start_point_y)
    draw_line_a = sd.get_vector(zero_point, start_angle, start_length, 1)
    draw_line_a.draw()
    draw_line_b = sd.get_vector(draw_line_a.end_point, start_angle + 72, start_length, 1)
    draw_line_b.draw()
    draw_line_c = sd.get_vector(draw_line_b.end_point, start_angle + 144, start_length, 1)
    draw_line_c.draw()
    draw_line_d = sd.get_vector(draw_line_c.end_point, start_angle + 216, start_length, 1)
    draw_line_d.draw()
    draw_line_e = sd.get_vector(draw_line_d.end_point, start_angle + 288, start_length, 1)
    draw_line_e.draw()


drawing_pentagon(400, 400, 30, 75)


def drawing_hexagon(start_point_x, start_point_y, start_angle, start_length):
    zero_point = sd.get_point(start_point_x, start_point_y)
    draw_line_a = sd.get_vector(zero_point, start_angle, start_length, 1)
    draw_line_a.draw()
    draw_line_b = sd.get_vector(draw_line_a.end_point, start_angle + 60, start_length, 1)
    draw_line_b.draw()
    draw_line_c = sd.get_vector(draw_line_b.end_point, start_angle + 120, start_length, 1)
    draw_line_c.draw()
    draw_line_d = sd.get_vector(draw_line_c.end_point, start_angle + 180, start_length, 1)
    draw_line_d.draw()
    draw_line_e = sd.get_vector(draw_line_d.end_point, start_angle + 240, start_length, 1)
    draw_line_e.draw()
    draw_line_f = sd.get_vector(draw_line_e.end_point, start_angle + 300, start_length, 1)
    draw_line_f.draw()


drawing_hexagon(150, 400, 40, 75)

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

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
