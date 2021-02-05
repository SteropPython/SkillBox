# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1000, 1000)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

startPointX = 50
startPointY = 50
finishPointX = 350
finishPointY = 450
for i in range(7):
    currentColor = rainbow_colors[i]
    startPoint = sd.get_point(startPointX, startPointY)
    endPoint = sd.get_point(finishPointX, finishPointY)
    sd.line(start_point = startPoint, end_point = endPoint, color=currentColor, width = 15)
    startPointX += 15
    finishPointX += 15

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
