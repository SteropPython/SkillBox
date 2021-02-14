import simple_draw as sd


def draw_tree(start_point=sd.get_point(600, 0), angle=90, length=130, color=sd.COLOR_DARK_GREEN, width=3):

    if length < 10:
        return

    if length < 25:
        color = sd.COLOR_GREEN
        width = 1

    vector = sd.Vector(start_point, angle, length, width)
    vector.draw(color)
    draw_tree(vector.end_point, angle-30, length*0.75)
    draw_tree(vector.end_point, angle+30, length*0.75)
