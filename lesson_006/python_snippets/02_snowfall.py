import simple_draw as sd

sd.resolution = (1000, 1000)

snowflake_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


#  создать_снежинки(N) - создает N снежинок

snowflake_points = []


def get_snowflake_point(count):
    while count > 0:
        snowflake_points.append(sd.random_point())
        count -= 1

    return snowflake_points

#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color


def paint_snowflakes(color):
    for i in range(len(snowflake_points)):
        sd.snowflake(snowflake_points[i], 25, color)


def snowflakes_step():
    for i in range(len(snowflake_points)):
        sd.snowflake(snowflake_points[i], 25, sd.background_color)


get_snowflake_point(5)

paint_snowflakes(sd.COLOR_RED)

for i in range(len(snowflake_points)):
    print(snowflake_points[i])

for i in range(len(snowflake_points)):
    snowflake_points[i](Po)
    print(snowflake_points[i])

snowflakes_step()

sd.pause()