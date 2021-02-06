# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

simple_draw.resolution = (1000, 1000)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

# def printSmile(startPointX, startPointY, color):

#     colorSmile = simple_draw.random_color() # for more beauty

#     pointSmile = simple_draw.get_point(startPointX, startPointY)
#     radiusSmaile = 66

#     eyeLeft = simple_draw.get_point(startPointX - 20, startPointY + 20)
#     eyeRight = simple_draw.get_point(startPointX + 20, startPointY + 20)
#     eyeRadius = 6

#     lipCornerLeft = simple_draw.get_point(startPointX - 20, startPointY - 20)
#     lipCornerRight = simple_draw.get_point(startPointX + 20, startPointY - 20)
#     lipCornerCenter = simple_draw.get_point(startPointX, startPointY - 40)


#     simple_draw.circle(pointSmile, radiusSmaile, colorSmile, 2)

#     simple_draw.circle(eyeLeft, eyeRadius, 2)

#     simple_draw.circle(eyeRight, eyeRadius, 2)

#     simple_draw.lines((lipCornerLeft, lipCornerCenter, lipCornerRight), True, 2)

# printSmile(200, 300, 'COLOR_ORANGE')


def printSmileRandom():

    for _ in range(100):

        colorSmile = simple_draw.random_color()

        pointSmile = simple_draw.random_point()
        
        radiusSmaile = 66

        startPointX = pointSmile.x

        startPointY = pointSmile.y

        eyeLeft = simple_draw.get_point(startPointX - 20, startPointY + 20)
        eyeRight = simple_draw.get_point(startPointX + 20, startPointY + 20)
        eyeRadius = 6

        lipCornerLeft = simple_draw.get_point(startPointX - 20, startPointY - 20)
        lipCornerRight = simple_draw.get_point(startPointX + 20, startPointY - 20)
        lipCornerCenter = simple_draw.get_point(startPointX, startPointY - 40)


        simple_draw.circle(pointSmile, radiusSmaile, colorSmile, 2)

        simple_draw.circle(eyeLeft, eyeRadius, colorSmile, 2)

        simple_draw.circle(eyeRight, eyeRadius, colorSmile, 2)

        simple_draw.lines((lipCornerLeft, lipCornerCenter, lipCornerRight), colorSmile, True, 2)


printSmileRandom()

simple_draw.pause()
