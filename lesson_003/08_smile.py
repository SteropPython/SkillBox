# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

simple_draw.resolution = (1000, 1000)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

def printSmile(startPointX, startPointY, color):

    colorSmile = simple_draw.random_color() # for more beauty

    pointSmile = simple_draw.get_point(startPointX, startPointY)
    radiusSmaile = 66

    eyeLeft = simple_draw.get_point(startPointX - 20, startPointY + 20)
    eyeRight = simple_draw.get_point(startPointX + 20, startPointY + 20)
    eyeRadius = 6

    lipCornerLeft = simple_draw.get_point(startPointX - 20, startPointY - 20)
    lipCornerRight = simple_draw.get_point(startPointX + 20, startPointY - 20)
    lipCornerCenter = simple_draw.get_point(startPointX, startPointY - 40)


    simple_draw.circle(center_position = pointSmile, radius = radiusSmaile, color = colorSmile, width = 2)

    simple_draw.circle(center_position = eyeLeft, radius = eyeRadius, width = 2)

    simple_draw.circle(center_position = eyeRight, radius = eyeRadius, width = 2)

    simple_draw.lines((lipCornerLeft, lipCornerCenter, lipCornerRight), closed=True, width=2)

printSmile(200, 300, 'COLOR_ORANGE')

simple_draw.pause()
