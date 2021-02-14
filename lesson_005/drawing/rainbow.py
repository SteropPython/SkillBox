import simple_draw as sd


def draw_rainbow(point_start_rainbow = sd.get_point(300, 0)):

    rainbow_colors = (sd.COLOR_RED,
                      sd.COLOR_ORANGE,
                      sd.COLOR_YELLOW,
                      sd.COLOR_GREEN,
                      sd.COLOR_CYAN,
                      sd.COLOR_BLUE,
                      sd.COLOR_PURPLE)

    radius_rainbow = 1500

    for i in range(7):
        current_color = rainbow_colors[i]
        sd.circle(point_start_rainbow, radius_rainbow, current_color, 20)
        radius_rainbow += 20

