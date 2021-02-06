# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код

figure_color = (
    sd.COLOR_RED,
    sd.COLOR_ORANGE,
    sd.COLOR_YELLOW,
    sd.COLOR_GREEN,
    sd.COLOR_CYAN,
    sd.COLOR_BLUE,
    sd.COLOR_PURPLE
)


def draw_line(sides, start, stop, angle, length, width, colored):

    decode_color = figure_color[colored]

    zero_point = sd.get_point(start, stop)

    amount_sides_angle = int(360 / sides)

    for i in range(0, 360, amount_sides_angle):
        draw_lines = sd.vector(zero_point, angle, length, decode_color, width)
        zero_point = sd.get_point(draw_lines.x, draw_lines.y)
        angle += amount_sides_angle


def drawing_figure(start_point_x, start_point_y, start_angle, start_length):

    user_color = {
        1: 'Red',
        2: 'Orange',
        3: 'Yellow',
        4: 'Green',
        5: 'Cyan',
        6: 'Blue',
        7: 'Purple'
    }

    draw_sides = int(input('How many sides the figure should have? (more than two)\n', ))

    draw_width = int(input('How width of sides the figure should have?\n', ))

    for i in user_color:
        print(i, '=>', user_color[i])

    draw_color = int(input('Select number of color for figure:\n', )) - 1

    draw_line(draw_sides, start_point_x, start_point_y, start_angle, start_length, draw_width, draw_color)


drawing_figure(150, 150, 10, 50)

sd.pause()
