# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

simple_draw.resolution = (1000, 1000)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

startPointX = 0
startPointY = 0
finishPointX = simple_draw.resolution[0]
finishPointY = simple_draw.resolution[1]
brickWidth = 100
brickHight = 50
brickStep = 0

for startPointY in range(0, finishPointY, brickHight):
    for startPointX in range(0, finishPointX, brickWidth):
        if brickStep % 2 == 0:
            startPointX -= brickHight
        startPoint = simple_draw.get_point(startPointX, startPointY)
        endPoint = simple_draw.get_point(startPointX + brickWidth, startPointY + brickHight)
        colorRectangle = simple_draw.random_color()
        simple_draw.rectangle(startPoint, endPoint, colorRectangle, 2)
        startPointX += brickWidth
    startPointY += brickHight
    startPointX = 0
    brickStep += 1
    
    

simple_draw.pause()
