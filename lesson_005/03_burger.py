# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# TODO здесь ваш код

def bun():
    add_bun = 'bun'
    print('And now we add -', add_bun)
    return add_bun


def cutlet():
    add_cutlet = 'cutlet'
    print('And now we add -', add_cutlet)
    return add_cutlet


def cucumber():
    add_cucumber = 'cucumber'
    print('And now we add -', add_cucumber)
    return add_cucumber


def tomato():
    add_tomato = 'tomato'
    print('And now we add -', add_tomato)
    return add_tomato


def mayonnaise():
    add_mayonnaise = 'mayonnaise'
    print('And now we add -', add_mayonnaise)
    return add_mayonnaise


def cheese():
    add_cheese = 'cheese'
    print('And now we add -', add_cheese)
    return add_cheese


def jalapeno():
    add_jalapeno = 'jalapeno'
    print('And now we add -', add_jalapeno)
    return add_jalapeno


def get_double_cheeseburger():
    recipe = [bun(),
              cutlet(),
              cucumber(),
              tomato(),
              mayonnaise(),
              cheese()]

    double_cheeseburger = ', '.join(recipe)

    return double_cheeseburger


def get_red_hot_cheeseburger():
    recipe = [bun(),
              cutlet(),
              jalapeno(),
              cucumber(),
              jalapeno(),
              tomato(),
              jalapeno(),
              mayonnaise(),
              jalapeno(),
              cheese()]
    red_hot_cheeseburger = ', '.join(recipe)

    return red_hot_cheeseburger


print('\nDouble cheeseburger recipe:', get_double_cheeseburger(), '\n')

print('\nDouble cheeseburger recipe:', get_red_hot_cheeseburger(), '\n')
