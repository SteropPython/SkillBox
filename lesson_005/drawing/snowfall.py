# -*- coding: utf-8 -*-

import simple_draw as sd
import random


def draw_snowfall(count=999, start_point=50, end_point=200, earth=100):

    snowfall_points_tuple = []

    for i in range(count):
        snowfall_points_tuple.append(sd.get_point(sd.random_point().x, sd.resolution[1]))

    for _ in range(count):
        while True:
            if sd.user_want_exit():
                break
            sd.snowflake(snowfall_points_tuple[_], 15)
            if snowfall_points_tuple[_].y < earth:
                break
            sd.snowflake(snowfall_points_tuple[_], 15, sd.background_color)
            snowfall_points_tuple[_].y -= 10
        #sd.sleep(0.05)

    #sd.finish_drawing()

        # for i in range(10):
        #     sd.snowflake(snowfall_points_tuple[_], 25)
        #     # if i == 5:
        #     #     break
        #     #
        #     #    sd.snowflake(snowfall_points_tuple[_], 25, sd.background_color)
        #     snowfall_points_tuple[_].y -= 10
        #
        #     print(i)
        #
        #
        #     #i += 10
        # print('snowflake {}'.format(_))


        # while snowfall_points_tuple[_].y > 0:
        #     #print(snowfall_points_tuple[_].y)
        #     sd.snowflake(snowfall_points_tuple[_], 25)
        #     sd.snowflake(snowfall_points_tuple[_], 25, sd.background_color)
        #     snowfall_points_tuple[_].y -= 1
        #print('X =', snowfall_points_tuple[_].x, 'Y =', snowfall_points_tuple[_].y)

    # def snowfall_print(point, step):
    #     lengths = 25
    #     while point.y > earth:
    #         sd.snowflake(point, lengths)
    #         if point.y < earth + step * 2:
    #             break
    #         sd.snowflake(point, lengths, sd.background_color)
    #         point.y -= step
    #
    # snowfall_points_tuple = []
    # snowfall_lengths_tuple = []
    # snowfall_step_snowfall = 5
    # # for i in range(count):
    # #     snowfall_lengths_tuple.append(random.randint(15, 25))
    #
    # for i in range(count):
    #     snowfall_points_tuple.append(sd.get_point(random.randint(start_point, end_point), sd.resolution[1]))
    #
    # for i in range(count):
    #     snowfall_print(snowfall_points_tuple[i], snowfall_step_snowfall)


draw_snowfall()

sd.pause()

