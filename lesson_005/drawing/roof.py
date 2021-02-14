import simple_draw as sd


def draw_roof(point_start=sd.get_point(0, 0), point_middle=sd.get_point(150, 150), point_finish=sd.get_point(300, 0)):
    points = [point_start, point_middle, point_finish]
    sd.polygon(points, width=0, color=sd.COLOR_DARK_PURPLE)