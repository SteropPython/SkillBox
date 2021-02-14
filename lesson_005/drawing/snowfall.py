# -*- coding: utf-8 -*-

import simple_draw as sd
import random


def draw_snowfall(count=10, start_point=50, end_point=200, earth=100):

    def snowfall_print(point, step):
        lengths = 25
        while point.y > earth:
            sd.snowflake(point, lengths)
            if point.y < earth + step * 2:
                break
            sd.snowflake(point, lengths, sd.background_color)
            point.y -= step

    snowfall_points_tuple = []
    snowfall_lengths_tuple = []
    snowfall_step_snowfall = 5
    # for i in range(count):
    #     snowfall_lengths_tuple.append(random.randint(15, 25))

    for i in range(count):
        snowfall_points_tuple.append(sd.get_point(random.randint(start_point, end_point), sd.resolution[1]))

    for i in range(count):
        snowfall_print(snowfall_points_tuple[i], snowfall_step_snowfall)

#
# draw_snowfall()
#
# sd.pause()

