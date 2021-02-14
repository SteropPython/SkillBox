# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код

import simple_draw as sd
import drawing.rainbow as mod_rainbow
import drawing.tree as mod_tree
import drawing.wall as mod_wall
import drawing.roof as mod_roof
import drawing.snowfall as mod_snowfall

# set global resolution for picture
sd.resolution = (1920, 1080)


# set start point for rainbow (def x=300, y=0)
point_start_rainbow = sd.get_point(500, 0)


# set start point for tree (def x=300, y=0)
point_start_tree_1 = sd.get_point(1400, 0)
point_start_tree_2 = sd.get_point(1600, 50)

# set points for wall
start_wall_point = 400
hight_wall_point = 400
width_wall_point = 800

# set roof points
start_roof_point = sd.get_point(start_wall_point - 10, hight_wall_point)
finish_roof_point = sd.get_point(width_wall_point + 10, hight_wall_point)
middle_roof_point = sd.get_point(start_wall_point + (width_wall_point - start_wall_point) / 2,
                                 hight_wall_point + (width_wall_point - start_wall_point) / 2)


mod_rainbow.draw_rainbow(point_start_rainbow)

mod_tree.draw_tree(point_start_tree_1, length=130)
mod_tree.draw_tree(point_start_tree_2, length=60)

mod_wall.draw_wall(start_wall_point, finishPointX=width_wall_point, finishPointY=hight_wall_point)

mod_roof.draw_roof(start_roof_point, middle_roof_point, finish_roof_point)

mod_snowfall.draw_snowfall(earth=0)




sd.pause()



# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
